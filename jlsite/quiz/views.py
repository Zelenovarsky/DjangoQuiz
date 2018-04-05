from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Question, Quiz, UserResults, Answer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from urllib.parse import parse_qs
import json
# Create your views here.
class QuizView(generic.ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'quiz_list'

    def get_queryset(self):
        return Quiz.objects.all()

class QuizQuestionsView(generic.DetailView):
    model = Quiz
    template_name = 'quiz/quiz_take.html'


class UserFromView(View):
    form_class = UserForm
    template_name = 'registration/reg_form.html'

    # blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('quiz:index')
        return render(request, self.template_name, {'form': form})


class UserResultsView(View):

    def get(self, request):
        template_name = 'quiz/user_results.html'
        user = request.user

        context = {
            'user_results': UserResults.objects.filter(user__id=user.id),
        }
        return render(request, template_name, context)

    def post(self, request):
        answers = request.POST['answers']
        user_id = request.POST['user_id']
        quiz_id = request.POST['quiz_id']

        quiz = Quiz.objects.get(pk=quiz_id)
        questions = quiz.question_set.all()
        user_score = 0
        answers_dict = parse_qs(answers)
        for question in questions:
            if 'question{}'.format(question.id) in answers_dict:
                if ','.join(answers_dict['question{}'.format(question.id)]) == question.correct_answer:
                    user_score += 1

        UserResults.objects.create(
            quiz=quiz,
            score=user_score,
            user=User.objects.get(pk=user_id),
            answers=answers
        )
        return HttpResponse('')

def create_quiz(request):
    template_name = 'quiz/quiz_create.html'
    return render(request,template_name)

def save_quiz(request):
    if request.method == 'POST':
        quiz_name = request.POST['quiz_name']
        quiz_data = request.POST['quiz_data']

        quiz_data = json.loads(quiz_data)
        quiz = Quiz.objects.create(quiz_name=quiz_name)
        print(quiz_data)
        for key, value in quiz_data.items():
            print(value['type'])
            question = Question.objects.create(quiz=quiz, question_text=key, question_type=value['type'],
                                               correct_answer=','.join(value['correctAnswers']))
            for i in value['answers']:
                Answer.objects.create(question=question, choice_text=i)
    return HttpResponse('')



def logout_view(request):
    logout(request)
    return redirect('quiz:index')
