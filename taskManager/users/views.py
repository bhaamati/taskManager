from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProjectUpdateForm, TaskUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created. Now you can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class ProjDetailView(DetailView):
    model = Project

class ProjCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['projectTitle']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['projectTitle']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/taskManager/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['proj', 'taskTitle', 'taskDescription', 'completion']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['taskTitle', 'taskDescription', 'completion']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True
       

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/taskManager/'
    
    def test_func(self):
        return True

@login_required
def taskPage(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'users/taskPage.html', context)

@login_required
def completed(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'users/completed.html', context)