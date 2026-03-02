from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.department}"

    class Meta:
        ordering = ['-hire_date', 'name']
