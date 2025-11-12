import base64
import io
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, Count, Sum
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Question, Choice
from .serializers import QuestionSerializer, QuestionListSerializer, ChoiceSerializer
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
import json
import csv


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionListSerializer
        return QuestionSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.GET.get('q', '')
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        sort_by = request.GET.get('sort_by', 'pub_date')

        questions = Question.objects.all()

        # Фильтрация по тексту
        if query:
            questions = questions.filter(question_text__icontains=query)

        # Фильтрация по дате
        if date_from:
            questions = questions.filter(pub_date__gte=date_from)
        if date_to:
            questions = questions.filter(pub_date__lte=date_to)

        # Сортировка
        if sort_by == 'popularity':
            questions = questions.annotate(total_votes=Sum('choice__votes')).order_by('-total_votes')
        elif sort_by == 'votes':
            questions = questions.annotate(total_votes=Sum('choice__votes')).order_by('-total_votes')
        else:
            questions = questions.order_by('-pub_date')

        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        question = self.get_object()

        stats = {
            'question_id': question.id,
            'question_text': question.question_text,
            'total_votes': question.total_votes(),
            'choices': []
        }

        for choice in question.choice_set.all():
            stats['choices'].append({
                'choice_text': choice.choice_text,
                'votes': choice.votes,
                'percentage': choice.percentage()
            })

        return Response(stats)

    @action(detail=True, methods=['get'])
    def chart(self, request, pk=None):
        question = self.get_object()

        # Создание диаграммы
        choices = question.choice_set.all()
        choice_texts = [choice.choice_text for choice in choices]
        votes = [choice.votes for choice in choices]
        percentages = [choice.percentage() for choice in choices]

        # Создание столбчатой диаграммы
        plt.figure(figsize=(10, 6))
        bars = plt.bar(choice_texts, votes, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        plt.title(f'Результаты голосования: {question.question_text}')
        plt.xlabel('Варианты ответа')
        plt.ylabel('Количество голосов')
        plt.xticks(rotation=45, ha='right')

        # Добавление процентов на столбцы
        for bar, percentage in zip(bars, percentages):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                     f'{percentage:.1f}%', ha='center', va='bottom')

        plt.tight_layout()

        # Сохранение в base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        return Response({
            'chart': f'data:image/png;base64,{image_base64}',
            'question_id': question.id,
            'question_text': question.question_text
        })

    @action(detail=True, methods=['get'])
    def export_csv(self, request, pk=None):
        question = self.get_object()

        response = JsonResponse({
            'question_id': question.id,
            'question_text': question.question_text,
            'csv_data': self._generate_csv(question)
        })
        return response

    @action(detail=True, methods=['get'])
    def export_json(self, request, pk=None):
        question = self.get_object()

        export_data = {
            'question_id': question.id,
            'question_text': question.question_text,
            'pub_date': question.pub_date.isoformat(),
            'total_votes': question.total_votes(),
            'choices': []
        }

        for choice in question.choice_set.all():
            export_data['choices'].append({
                'choice_text': choice.choice_text,
                'votes': choice.votes,
                'percentage': choice.percentage()
            })

        return Response(export_data)

    def _generate_csv(self, question):
        output = io.StringIO()
        writer = csv.writer(output)

        # Заголовок
        writer.writerow(['Question', question.question_text])
        writer.writerow(['Total Votes', question.total_votes()])
        writer.writerow([])
        writer.writerow(['Choice', 'Votes', 'Percentage'])

        # Данные
        for choice in question.choice_set.all():
            writer.writerow([
                choice.choice_text,
                choice.votes,
                f"{choice.percentage():.2f}%"
            ])

        return output.getvalue()


@api_view(['GET'])
def global_statistics(request):
    """Микросервис: Глобальная статистика по всем голосованиям"""
    total_questions = Question.objects.count()
    total_votes = sum(question.total_votes() for question in Question.objects.all())

    # Самые популярные голосования
    popular_questions = Question.objects.annotate(
        total_votes=Sum('choice__votes')
    ).order_by('-total_votes')[:5]

    popular_data = []
    for question in popular_questions:
        popular_data.append({
            'question_text': question.question_text,
            'total_votes': question.total_votes() or 0
        })

    return Response({
        'total_questions': total_questions,
        'total_votes': total_votes,
        'popular_questions': popular_data
    })

@api_view(['GET'])
def chart_image(request, pk):
    """Возвращает непосредственно PNG изображение"""
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    # Создание диаграммы (код из метода chart)
    choices = question.choice_set.all()
    choice_texts = [choice.choice_text for choice in choices]
    votes = [choice.votes for choice in choices]
    percentages = [choice.percentage() for choice in choices]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(choice_texts, votes, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    plt.title(f'Результаты голосования: {question.question_text}')
    plt.xlabel('Варианты ответа')
    plt.ylabel('Количество голосов')
    plt.xticks(rotation=45, ha='right')

    for bar, percentage in zip(bars, percentages):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                 f'{percentage:.1f}%', ha='center', va='bottom')

    plt.tight_layout()

    # Сохранение в HttpResponse
    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='png', dpi=100, bbox_inches='tight')
    plt.close()

    return response