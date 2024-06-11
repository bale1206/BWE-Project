from django.shortcuts import render
# Create your views here.

def index(request):
    context = {}
    return render(request,'pages/index.html', context)

def explorer(request):
    context = {}
    return render(request,'pages/explorer.html', context)

def login(request):
    context = {}
    return render(request,'pages/login.html', context)

def profile(request):
    context = {}
    return render(request,'pages/profile.html', context)

def register(request):
    context = {}
    return render(request,'pages/register.html', context)

def shoppingcart(request):
    context = {}
    return render(request,'pages/shoppingcart.html', context)




