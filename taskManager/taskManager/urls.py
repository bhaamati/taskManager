"""taskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include 
from users import views as user_views
from users.views import ProjCreateView, ProjUpdateView, ProjDetailView, ProjDeleteView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('completed/', user_views.completed, name='completed'),
    path('newProj/', ProjCreateView.as_view(), name='newProj'),
    path('newProj/<int:pk>/', ProjDetailView.as_view(), name='proj-detail'),
    path('newProj/<int:pk>/update/', ProjUpdateView.as_view(), name='proj-update'),
    path('newProj/<int:pk>/delete/', ProjDeleteView.as_view(), name='proj-delete'),
    path('newTask/', TaskCreateView.as_view(), name='newTask'),
    path('newTask/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('newTask/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('newTask/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('taskManager/', user_views.taskPage, name='taskPage'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('tasks.urls')),
]
