from django.shortcuts import render, redirect
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/login")
def index(request):
    if request.method == 'POST':
        task = request.POST.get('task').strip()
        if task:
            Todo.objects.create(text=task, users = request.user)
            return redirect('index')
        
    todo = Todo.objects.filter(users=request.user)
    context = {
        'todo': todo
    }
    return render(request, 'todoApp/index.html', context)

@login_required(login_url="/login")
def delete(request, id):
    todo = Todo.objects.get(id=id , users=request.user)
    todo.delete()
    return redirect('index')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "@ username and password is incorrect.")
            return render(request, 'todoApp/login.html')
        
    return render(request, 'todoApp/login.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        usern = User.objects.filter(username=username)
        if usern:
            messages.add_message(request, messages.ERROR, "username already exists.")
            return render(request, 'todoApp/register.html')
        
        useremail = User.objects.filter(email=email)
        if useremail:
            messages.add_message(request, messages.ERROR, "email already exists.")
            return render(request, 'todoApp/register.html')
        if password==cpassword:
            

            user = User.objects.create(username=username, first_name = first_name, last_name= last_name, email=email)
            user.set_password(password)
            user.save()
            return redirect('log_in')

    return render(request, 'todoApp/register.html')