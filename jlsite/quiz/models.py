from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('quiz:quiz-take', kwargs={'pk': self.pk})

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    TYPES = (
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
        ('text', 'text'),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, default=' ')
    pub_date = models.DateTimeField(auto_now=True)
    question_type = models.CharField(max_length=10, choices=TYPES, default='radio')
    correct_answer = models.TextField(default='')

    def __str__(self):
        return self.question_text


class UserResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    answers = models.TextField(default='')
    submission_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s's profile" % self.user


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(default='')
    explanation = models.TextField(default='yep')

    def __str__(self):
        return self.choice_text
