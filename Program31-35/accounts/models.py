from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='Student')

    def is_admin(self):
        return self.role == 'Admin'

    def is_teacher(self):
        return self.role == 'Teacher'

    def is_student(self):
        return self.role == 'Student'
