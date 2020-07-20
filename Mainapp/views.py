from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'Mainapp/register.html')

def login(request):
    return render(request,'Mainapp/login.html')
