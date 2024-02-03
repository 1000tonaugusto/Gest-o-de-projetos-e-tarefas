from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile
from .forms import ProfileForm


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile_update_form.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Deu certo")
            user = form.save()
            login(request, user)
            return redirect('home')
        
    form = UserCreationForm
    return render(request, 'users/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('logar')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm