from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

from .forms import RegisterForm


def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'registration/login.html', {'page': 'register', 'form': form})


def dont_have_acces(request):
    return render(request, 'home/dont-have-access.html')