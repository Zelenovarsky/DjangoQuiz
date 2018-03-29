from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Question, Quiz, UserResults
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from urllib.parse import parse_qs



class QuizView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'quiz_list'

    def get_queryset(self):
        return Quiz.objects.all()


class DetailView(generic.DetailView):
    model = Quiz
    template_name = 'polls/detail.html'

    def get_all_answers_string(self):
        return Quiz.question_set.all[1].id


class QuizQuestionsView(generic.DetailView):
    model = Quiz
    template_name = 'polls/detail.html'


class UserFromView(View):
    form_class = UserForm
    template_name = 'polls/reg_from.html'

    # blank form fo new user
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
                    return redirect('polls:index')
        return render(request, self.template_name, {'form': form})


class UserResultsView(View):

    def get(self,request):
        template_name = 'polls/all_user_results.html'
        user = request.user

        context = {
            'user_results' : UserResults.objects.filter(user__id = user.id),
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
            if ','.join(answers_dict['question{}'.format(question.id)]) == question.correct_answer:
                user_score += 1

        UserResults.objects.create(
            quiz=quiz,
            score=user_score,
            user=User.objects.get(pk=user_id),
            answers=answers
        )
        return HttpResponse('')


def save_user_input(request):
    if request.method == 'POST':
        answers = request.POST['answers']
        user_id = request.POST['user_id']
        quiz_id = request.POST['quiz_id']

        quiz = Quiz.objects.get(pk=quiz_id)
        questions = quiz.question_set.all()
        user_score = 0
        answers_dict = parse_qs(answers)
        for question in questions:
             if ','.join(answers_dict['question{}'.format(question.id)]) == question.correct_answer:
                 user_score+=1

        UserResults.objects.create(
            quiz = quiz,
            score = user_score,
            user=User.objects.get(pk=user_id),
            answers=answers
        )
        return HttpResponse('')



def logout_view(request):
    logout(request)
    return redirect('polls:index')


class QuizCreate(CreateView):
    model = Quiz
    fields = ['quiz_name']
# class Questionsview(generic.ListView):
#     model = Quiz
#     fields = ['question_text','pub_date']
#     template_name = 'polls/questions.html'


# def quiz_view(request):
#     all_quizzes = Quiz.objects.all()
#     context = {'all_quizzes': all_quizzes}
#     template_name = 'polls/quizzes.html'
#     return render(request, template_name, context)

#
#
# class IndexView(generic.ListView):
#     #
#     # template_name = 'polls/index.html'
#     # classontext_object_name = 'quiz_list'
#     model = Quiz
#     # def get_queryset(self):
#     #     """Return the last five published questions."""
#     #     return Quiz.objects.order_by()[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
