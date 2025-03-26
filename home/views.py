from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.user.is_authenticated:  # Check if already logged in
        return redirect('home')  # Redirect to home page

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'home/login.html')

@login_required  # Protect home page
def home_page(request):
    return render(request, 'home/home.html')
