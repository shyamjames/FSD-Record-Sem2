"""
Quick script to add sample employee data for pagination demonstration
Run: python Program36-38/add_sample_data.py
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from directory.models import Employee
from datetime import date, timedelta

# Sample employee data
employees_data = [
    {"name": "John Doe", "email": "john.doe@company.com", "department": "Engineering", "salary": 75000},
    {"name": "Jane Smith", "email": "jane.smith@company.com", "department": "Marketing", "salary": 65000},
    {"name": "Bob Johnson", "email": "bob.johnson@company.com", "department": "Engineering", "salary": 80000},
    {"name": "Alice Williams", "email": "alice.williams@company.com", "department": "HR", "salary": 60000},
    {"name": "Charlie Brown", "email": "charlie.brown@company.com", "department": "Sales", "salary": 70000},
    {"name": "Diana Prince", "email": "diana.prince@company.com", "department": "Engineering", "salary": 85000},
    {"name": "Eve Davis", "email": "eve.davis@company.com", "department": "Marketing", "salary": 62000},
    {"name": "Frank Miller", "email": "frank.miller@company.com", "department": "Engineering", "salary": 78000},
    {"name": "Grace Lee", "email": "grace.lee@company.com", "department": "Finance", "salary": 72000},
    {"name": "Henry Wilson", "email": "henry.wilson@company.com", "department": "IT", "salary": 68000},
    {"name": "Ivy Chen", "email": "ivy.chen@company.com", "department": "Engineering", "salary": 82000},
    {"name": "Jack Taylor", "email": "jack.taylor@company.com", "department": "Sales", "salary": 71000},
    {"name": "Karen Martinez", "email": "karen.martinez@company.com", "department": "HR", "salary": 61000},
    {"name": "Leo Anderson", "email": "leo.anderson@company.com", "department": "Marketing", "salary": 67000},
    {"name": "Maya Thomas", "email": "maya.thomas@company.com", "department": "Engineering", "salary": 79000},
]

def add_employees():
    print("Adding sample employees to database...")
    
    # Clear existing employees
    Employee.objects.all().delete()
    print("Cleared existing employees")
    
    # Add new employees
    base_date = date(2023, 1, 1)
    for i, emp_data in enumerate(employees_data):
        emp_data['hire_date'] = base_date + timedelta(days=i*30)
        employee = Employee.objects.create(**emp_data)
        print(f"Added: {employee.name} - {employee.department}")
    
    print(f"\n✓ Successfully added {len(employees_data)} employees!")
    print("\nNow you can test:")
    print("- Pagination: Visit http://127.0.0.1:8000/ (5 employees per page)")
    print("- Search: Try searching 'Engineering' or 'John'")
    print("- Pages: ?page=1, ?page=2, ?page=3")

if __name__ == '__main__':
    add_employees()
