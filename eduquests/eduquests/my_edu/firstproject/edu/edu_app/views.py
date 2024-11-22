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

def class1(request):
    return render(request, 'edu_app/class1.html')

def belajarmenyenangkan(request):
    return render(request, 'edu_app/belajarmenyenangkan.html')

def minatbakat(request):
    return render(request, 'edu_app/minatbakat.html')

def manajemenwaktu(request):
    return render(request, 'edu_app/manajemenwaktu.html')

def materimodul1(request):
    return render(request, 'edu_app/materimodul1.html')

def Quizmodul1(request):
    return render(request, 'edu_app/Quizmodul1.html')

def Quizmodul2(request):
    return render(request, 'edu_app/Quizmodul2.html')
