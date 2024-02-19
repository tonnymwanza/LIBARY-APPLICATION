from django.urls import path
from accounts_app import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login' ,views.login, name='login'),
]