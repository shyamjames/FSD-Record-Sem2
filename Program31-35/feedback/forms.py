from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message', 'rating']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is this regarding?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Type your feedback here...'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
        }
