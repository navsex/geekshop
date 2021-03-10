from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from authapp.forms import UserLoginForm, UserCreationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(request('index'))
    context = {
        'title': 'GeekShop - Авторизация',
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'GeekShop - Регистрация',
    }
    return render(request, 'authapp/register.html', context)