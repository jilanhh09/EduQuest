from django.urls import path, include
from . import views

app_name = "edu_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('ourteam', views.ourteam, name='ourteam'),
    path('course', views.course, name='course'),
    path('login', views.login, name='login'),  
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout_view, name='logout'), 
]
