from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Task

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projectTitle']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super.form_valid(form)
        
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['proj', 'taskTitle', 'taskDescription', 'completion']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super.form_valid(form)

