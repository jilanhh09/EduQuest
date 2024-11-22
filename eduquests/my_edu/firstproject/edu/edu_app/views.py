from django.shortcuts import render, redirect
from .forms import signupform
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User, auth

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu_app:login')
    else:
        form = signupform()
    return render(request, 'edu_app/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('edu_app:dashboard')
        else:
            return render(request, 'edu_app/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'edu_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('edu_app:home')

def home(request):
    return render(request, 'edu_app/home.html')

def ourteam(request):
    return render(request, 'edu_app/ourteam.html')

def course(request):
    return render(request, 'edu_app/course.html')

def dashboard(request):
    return render(request, 'edu_app/dashboard.html')
