from django.urls import path
from django.contrib.auth.views import logout

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.QuizView.as_view(), name='index'),
    path('register/', views.UserFromView.as_view(), name='register'),
    path('<int:pk>', views.QuizQuestionsView.as_view(), name='quiz-take'),

    #/quiz/add
    # path('quiz/add/', views.QuizCreate.as_view(), name='quiz-create'),
    path('quiz/create', views.create_quiz,name='quiz-create'),
    path('quiz/save', views.save_quiz, name='save'),
    path('quiz/results', views.UserResultsView.as_view(), name='kek'),

]