from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.urls import reverse
from django.contrib import messages  # optional, for user feedback

def index(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")  # optional
            return redirect('index')  # use named URL

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'index.html', context)


def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")  # optional
            return redirect('index')

    context = {'form': form, 'task': task}
    return render(request, 'update.html', context)


def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('index')  # use the named URL of your index view

    context = {'task': task}
    return render(request, 'delete.html', context)