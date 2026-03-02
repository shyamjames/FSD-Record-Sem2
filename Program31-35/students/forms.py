from django import forms
from .models import StudentProfile

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'email', 'enrollment_number', 'course', 'date_of_birth']
        widgets = {
             'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
             'email': forms.EmailInput(attrs={'class': 'form-control'}),
             'enrollment_number': forms.TextInput(attrs={'class': 'form-control'}),
             'course': forms.TextInput(attrs={'class': 'form-control'}),
        }
