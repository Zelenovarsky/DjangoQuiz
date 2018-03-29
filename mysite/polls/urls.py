from django.urls import path
from django.contrib.auth.views import logout

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuizView.as_view(), name='index'),
    path('register/', views.UserFromView.as_view(), name='register'),
    # path('logout/', views.logout_view, name='logout'),
    # path('login/', views.logout_view, name='login'),
    # path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.QuizQuestionsView.as_view(), name='detail'),

    #polls/quiz/add
    path('quiz/add/', views.QuizCreate.as_view(), name='quiz-create'),
    # path('quiz/results', views.save_user_input, name='kek'),
    path('quiz/results', views.UserResultsView.as_view(), name='kek'),

]