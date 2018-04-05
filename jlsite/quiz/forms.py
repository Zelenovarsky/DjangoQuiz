from django import forms
from .models import Quiz, Question, Answer
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice_text']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
