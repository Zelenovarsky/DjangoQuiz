from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/polls'}),
]
