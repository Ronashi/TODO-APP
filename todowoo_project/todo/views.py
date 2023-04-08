from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signuser(request):
    
    return render(request, 'todo/signuser.html', {'form':UserCreationForm()})
     