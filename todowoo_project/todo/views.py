from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import user
# Create your views here.


def signuser(request):
    if request.method == 'GET':
    return render(request, 'todo/signuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2]:
            user =  User.object.create_user(request.POST['password1'])
            user.save()
            
        
     
     