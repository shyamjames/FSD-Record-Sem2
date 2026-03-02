from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import datetime

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Program 35: Implementing Session Management explicitly
            # Set custom session variables upon login
            request.session['login_time'] = str(datetime.datetime.now())
            request.session['user_role'] = user.role
            
            return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    # Retrieve session data to demonstrate Program 35
    login_time = request.session.get('login_time', 'Unknown')
    role = request.session.get('user_role', 'Unknown')
    
    context = {
        'login_time': login_time,
        'role': role,
        'session_expiry': request.session.get_expiry_age(),
    }
    return render(request, 'accounts/home.html', context)
