from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
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

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Set session variables upon registration
            request.session['login_time'] = str(datetime.datetime.now())
            request.session['user_role'] = user.role
            
            # Redirect based on role
            if user.role == 'Admin':
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def home_view(request):
    # Retrieve session data to demonstrate Program 35
    login_time = request.session.get('login_time', 'Unknown')
    role = request.session.get('user_role', 'Unknown')
    
    # Redirect to appropriate dashboard based on role
    if request.user.role == 'Admin':
        return redirect('admin_dashboard')
    else:
        return redirect('student_dashboard')


@login_required
def admin_dashboard(request):
    context = {
        'login_time': request.session.get('login_time', 'Unknown'),
        'role': request.user.role,
    }
    return render(request, 'accounts/admin_dashboard.html', context)


@login_required
def student_dashboard(request):
    context = {
        'login_time': request.session.get('login_time', 'Unknown'),
        'role': request.user.role,
    }
    return render(request, 'accounts/student_dashboard.html', context)


@login_required
def session_management(request):
    """
    Program 35: Comprehensive Session Management
    Demonstrates session creation, reading, updating, and deletion
    """
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            # Add custom session variable
            key = request.POST.get('key')
            value = request.POST.get('value')
            if key and value:
                request.session[key] = value
                request.session.modified = True
        
        elif action == 'delete':
            # Delete specific session variable
            key = request.POST.get('key')
            if key in request.session:
                del request.session[key]
                request.session.modified = True
        
        elif action == 'clear_custom':
            # Clear all custom session variables (keep auth-related ones)
            keys_to_delete = []
            for key in request.session.keys():
                if key not in ['_auth_user_id', '_auth_user_backend', '_auth_user_hash']:
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                del request.session[key]
            request.session.modified = True
        
        elif action == 'update_expiry':
            # Update session expiry time
            expiry_seconds = request.POST.get('expiry_seconds')
            if expiry_seconds:
                request.session.set_expiry(int(expiry_seconds))
        
        return redirect('session_management')
    
    # Get all session data
    session_data = {}
    for key in request.session.keys():
        session_data[key] = request.session[key]
    
    # Get session metadata
    session_key = request.session.session_key
    expiry_age = request.session.get_expiry_age()
    expiry_date = request.session.get_expiry_date()
    
    context = {
        'session_data': session_data,
        'session_key': session_key,
        'expiry_age': expiry_age,
        'expiry_date': expiry_date,
        'login_time': request.session.get('login_time', 'Unknown'),
        'user_role': request.session.get('user_role', 'Unknown'),
    }
    
    return render(request, 'accounts/session_management.html', context)


# Simple Session Demo Views (Text Output)
def session_set(request):
    """Set a session variable"""
    request.session['username'] = 'Jiyo'
    return render(request, 'accounts/session_output.html', {
        'message': 'Session Set Successfully'
    })


def session_get(request):
    """Get a session variable"""
    username = request.session.get('username', None)
    if username:
        message = f'Username: {username}'
    else:
        message = 'Username: No Session Found'
    
    return render(request, 'accounts/session_output.html', {
        'message': message
    })


def session_delete(request):
    """Delete a session variable"""
    if 'username' in request.session:
        del request.session['username']
    
    return render(request, 'accounts/session_output.html', {
        'message': 'Session Deleted'
    })
