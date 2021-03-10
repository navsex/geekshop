from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from authapp.forms import UserLoginForm, UserCreationForm


def login(request):
    context = {
        'title': 'GeekShop - Авторизация',
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'GeekShop - Регистрация',
    }
    return render(request, 'authapp/register.html', context)