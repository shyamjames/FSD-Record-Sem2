from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Employee

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Strong Password', 'class': 'form-control'}), 
        min_length=8
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}), 
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
             self.add_error('password_confirm', "Passwords do not match.")
        
        return cleaned_data

class EmployeeForm(forms.ModelForm):
    """
    Program 37: Form Validation
    Demonstrates custom field-level validation and error handling logic.
    """
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary and salary < 0:
            raise ValidationError("Salary cannot be a negative value. Please enter a valid number.")
        if salary and salary < 10000:
            raise ValidationError("Minimum wage standards require a salary of at least 10,000.")
        return salary
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@company.com'):
             raise ValidationError("This directory is restricted to @company.com email addresses.")
        return email
