from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm

def home(request):
    return render(request, 'index.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home or dashboard page
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = LoginForm()  # If GET request, just show the empty form

    return render(request, 'login.html', {'form': form})


