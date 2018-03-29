from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.quiz_name



class Question(models.Model):
    TYPES = (
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
        ('text', 'text'),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
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

# class User(AbstractUser):
#     gender = models.BooleanField(default=False)
#     def __str__(self):
#         return self.username

# class FreeAnswer(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     answer_text = models.TextField
#     question_answer = models.TextField
#
#     def __str__(self):
#         return self.answer_text


# ########################
# class User(models.Model):
#     username = models.CharField(max_length=30)
#     is_admin = models.BooleanField()
#     def __str__(self):
#         return self.username
#
# class Quiz(models.Model):
#     quiz_text = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.quiz_text
#
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#
#     # def was_published_recently(self):
#     #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     correct_flag = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.choice_text
