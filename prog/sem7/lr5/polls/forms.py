from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Question, Choice


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label='Question Text',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question here'})
    )
    choices = forms.CharField(
        label='Choices (one per line)',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter each choice on a separate line',
            'rows': 5
        }),
        help_text='Enter each choice on a separate line'
    )

    def clean_choices(self):
        choices_text = self.cleaned_data['choices']
        choices_list = [choice.strip() for choice in choices_text.split('\n') if choice.strip()]

        if len(choices_list) < 2:
            raise ValidationError('Please provide at least 2 choices.')

        if len(choices_list) > 10:
            raise ValidationError('Please provide no more than 10 choices.')

        if len(choices_list) != len(set(choices_list)):
            raise ValidationError('Please remove duplicate choices.')

        return choices_text


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})