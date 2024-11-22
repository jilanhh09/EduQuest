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
    path('class1', views.class1, name='class1'), 
    path('belajarmenyenangkan', views.belajarmenyenangkan, name='belajarmenyenangkan'), 
    path('minatbakat', views.minatbakat, name='minatbakat'), 
    path('manajemenwaktu', views.manajemenwaktu, name='manajemenwaktu'),
    path('materimodul1', views.materimodul1, name='materimodul1'),
    path('Quizmodul1', views.Quizmodul1, name='Quizmodul1'), 
    path('Quizmodul2', views.Quizmodul2, name='Quizmodul2') 
]
