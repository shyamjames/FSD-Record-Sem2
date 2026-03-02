from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required, teacher_required
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages

@login_required
def submit_feedback(request):
    """Allow any logged in user (usually Students) to submit feedback"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Your feedback has been successfully submitted!')
            return redirect('home')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/submit.html', {'form': form})

@teacher_required
def list_feedback(request):
    """Allow Teachers and Admins to view all feedback"""
    feedbacks = Feedback.objects.select_related('user').all()
    return render(request, 'feedback/list.html', {'feedbacks': feedbacks})
