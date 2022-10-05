from .forms import SignupForm, SigninForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout

# Signup View Function
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Your account has been created successfully. Please sign in.")
        else:
            fm = SignupForm()
        return render(request, 'my_user/signup.html', {'form':fm})

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            fm = SigninForm(request=request, data=request.POST)
            if fm.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                print(username, password)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome {username}.')
                    return HttpResponseRedirect('/')
        else:
            fm = SigninForm()
        return render(request, 'my_user/signin.html', {'form':fm})

# IMPORTANT --> Can not use logout as this function name because it clashes with logout builtin function.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'my_user/home.html')
    else:
        return redirect('signin')

