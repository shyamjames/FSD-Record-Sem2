from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def admin_required(function=None, redirect_field_name=None, login_url=None):
    """Decorator for views that checks that the user is logged in and is an Admin."""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def teacher_required(function=None, redirect_field_name=None, login_url=None):
    """Decorator for views that checks that the user is logged in and is a Teacher (or Admin)."""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.is_teacher() or u.is_admin()),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def student_required(function=None, redirect_field_name=None, login_url=None):
    """Decorator for views that checks that the user is logged in and is a Student."""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
