from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request):
    tasks=Task.objects.all()
    return render(request,'todo/home.html',{'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')
