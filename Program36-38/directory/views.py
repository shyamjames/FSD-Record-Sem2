from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    """
    Program 38: Secure Authentication System with Password Hashing.
    Demonstrates manual usage of make_password to securely hash the raw password string
    before finalizing the save to the database, ensuring no plaintext passwords exist.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Don't save to db yet
            user = form.save(commit=False)
            
            # Extract raw password
            raw_password = form.cleaned_data.get('password')
            
            # Securely hash the password using Django's built in hashing framework (PBKDF2 by default)
            secured_password = make_password(raw_password)
            
            # Assign hashed password and save
            user.password = secured_password
            user.save()
            
            messages.success(request, f"Account created for {user.username}! You can now login securely.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'directory/register.html', {'form': form})

def login_view(request):
    """ Standard Django auth view that leverages Check_Password() underneath """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in securely as {username}.")
                return redirect('employee_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'directory/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have securely logged out.")
    return redirect('login')

from django.db.models import Q
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

@login_required
def employee_list(request):
    """
    Program 36: Pagination and Search Feature.
    Uses Q objects for robust querying across name or department,
    and Django's Paginator to split result sets.
    """
    query = request.GET.get('q', '')
    
    if query:
        # Search by either Name or Department using Q objects
        employees = Employee.objects.filter(
            Q(name__icontains=query) | Q(department__icontains=query)
        )
    else:
        employees = Employee.objects.all()
        
    # Paginate results - 5 employees per page
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'directory/employee_list.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def employee_create(request):
    """
    Program 37: Form Validation & Error Handling
    Catches potential DB integrity errors explicitly safely.
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Employee '{form.cleaned_data.get('name')}' added successfully.")
                return redirect('employee_list')
            except IntegrityError as e:
                # Fallback block mimicking explicit Db Error Handling logic
                messages.error(request, "Database Error: This record could not be saved uniquely.")
        else:
            messages.error(request, "Please correct the form validation errors below.")
    else:
        form = EmployeeForm()
        
    return render(request, 'directory/employee_form.html', {'form': form})

