from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# it use for redirection 
from django.urls import reverse_lazy


# Authenticated imports
from django.contrib.auth.views import LoginView

from .models import Task



class LoginPage(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    '''
    List view look for task_list (model_list) for the template create template task_list.html
    '''
    model = Task
    # by default we django give object_list context but we can rename thru context_object_model
    context_object_name = 'tasks'
    
    # here we are rename the template and telling that don't look for task_list look base/tasks.html
    template_name = 'base/tasks.html'


class TaskDetail(DetailView):
    '''
    1. List view look for task_detail (model_detail) for the template create template task_detail
    .html
    
    2. It pass Object as a context use in html  - {{object.title}} etc
    '''
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    # redirection to landing page
    success_url = reverse_lazy('tasks')
    # fields = ['title', 'description']
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
