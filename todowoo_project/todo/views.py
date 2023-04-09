from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                # Return an error message or redirect to a different page
                return redirect('user_exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                return redirect('homepage')
        else:
            # If the form is not valid, re-render the sign-up page with the errors shown
            return render(request, 'todo/signuser.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'todo/signuser.html', {'form': form})
