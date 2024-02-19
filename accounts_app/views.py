from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate
# Create your views here.

def registration(request): #the view to sign up users
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is in use, find another one')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password)
                return redirect('login')
        else:
            messages.error(request, 'the passwords given dont match')
            return redirect('registration')
    return render(request, 'registration.html')

def login(request): #the view to login the existing users
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid information. Try again')
            return redirect('login')
    return render(request, 'login.html')