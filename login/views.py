from django.http import HttpResponseRedirect
from django.shortcuts import render
from projects.models import Project
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm


def dashboard(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'login/login/projectindex.html', context)

def userregister(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, 'login/registration/register.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(request, username=u, password=p)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login/registration/login.html', {'form': form})
