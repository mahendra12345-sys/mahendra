
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Try again.")
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
    return redirect('home')


def home(request):
    return render(request, 'accounts/home.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Bus, Booking
from .forms import BookingForm


@login_required
def book_bus(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign user to booking
            booking.save()
            return redirect('home')

    else:
        form = BookingForm()

    buses = Bus.objects.all()
    return render(request, 'accounts/book_bus.html', {'form': form, 'buses': buses})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # TEMPORARY: Only for debugging
def my_view(request):
    if request.method == "POST":
        # Process form submission
        pass
    return render(request, 'my_template.html')


from django.shortcuts import redirect

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to Dashboard
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, 'accounts/login.html')
