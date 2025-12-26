from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Task
from .forms import TaskForm, UserRegisterForm


class TaskListView(LoginRequiredMixin, ListView):
    """
    Display list of tasks for the logged-in user.
    Supports filtering, searching, and sorting.
    """
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        
        # Filter by status
        status = self.request.GET.get('status')
        if status == 'completed':
            queryset = queryset.filter(completed=True)
        elif status == 'active':
            queryset = queryset.filter(completed=False)
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Sort functionality
        sort_by = self.request.GET.get('sort')
        if sort_by == 'priority':
            queryset = queryset.order_by('-priority', 'due_date')
        elif sort_by == 'due_date':
            queryset = queryset.order_by('due_date', '-priority')
        elif sort_by == 'created':
            queryset = queryset.order_by('-created_at')
        else:
            # Default ordering from model
            queryset = queryset.order_by('-priority', 'due_date', '-created_at')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.request.GET.get('status', 'all')
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_by'] = self.request.GET.get('sort', '')
        return context


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    Display detailed view of a single task.
    Only the task owner can view it.
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new task for the logged-in user.
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Task'
        return context


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update an existing task.
    Only the task owner can update it.
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Task'
        return context


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a task.
    Only the task owner can delete it.
    """
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    context_object_name = 'task'
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


class RegisterView(CreateView):
    """
    User registration view.
    Automatically logs in the user after successful registration.
    """
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Log in the user after registration
        login(self.request, self.object)
        return response


def logout_view(request):
    """
    Custom logout view to handle GET requests and redirect to login page.
    """
    logout(request)
    return redirect('login')
