from django.shortcuts import render

def login(request):
    context = {

    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {

    }
    return render(request, 'authapp/register.html', context)