from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import teacher_required
from .models import StudentProfile
from .forms import StudentForm

@teacher_required
def student_list(request):
    students = StudentProfile.objects.all().order_by('-created_at')
    return render(request, 'students/student_list.html', {'students': students})

@teacher_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sms_student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Add'})

@teacher_required
def student_update(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('sms_student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Edit', 'student': student})

@teacher_required
def student_delete(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('sms_student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
