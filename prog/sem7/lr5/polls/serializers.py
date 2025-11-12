from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'percentage']

    def get_percentage(self, obj):
        total_votes = obj.question.total_votes()
        if total_votes == 0:
            return 0
        return round((obj.votes / total_votes) * 100, 2)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices', 'total_votes']

    def get_total_votes(self, obj):
        return obj.total_votes()


class QuestionListSerializer(serializers.ModelSerializer):
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'total_votes']

    def get_total_votes(self, obj):
        return obj.total_votes()