from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import  login, logout, authenticate
from .forms import Todo_form

def home(request):
     return render(request, 'todo/home.html' )




def signupuser(request):
    if request.method =='GET':
         return render(request, 'todo/signuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
                 user.save()
                 login(request, user)
                 return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signuser.html', {'form': UserCreationForm(), 'error': 'Oops! username has already been used, choose another'})
        else :
            #pass didn't match
             return render(request, 'todo/signuser.html', {'form': UserCreationForm(), 'error': 'password mismatch'})
         
def  loginuser(request):
    if request.method =='GET':
        return render(request, 'todo/signuser.html', {'form': AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'], password=['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Invalid username or password'})
                

def  logoutuser(request):
        if request.method == 'POST':    
            logout(request)
            return redirect('home')
        
 
def currenttodos(request):
    return render(request, 'todo/currenttodos.html', {'form': UserCreationForm()})   

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':Todo_form})
    else:
        pass
  