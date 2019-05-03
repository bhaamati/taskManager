from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib import messages

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s" % (self.projectTitle)
    
    def get_absolute_url(self):
        return reverse('proj-detail', kwargs={'pk': self.pk})

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name="project_set")
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    completion = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('taskTitle',)