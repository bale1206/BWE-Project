from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def shoppingcart(request):
    context = {}
    return render(request,'pages/shoppingcart.html', context)