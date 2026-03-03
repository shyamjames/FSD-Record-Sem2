from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('session-management/', views.session_management, name='session_management'),
    
    # Simple Session Demo URLs
    path('set/', views.session_set, name='session_set'),
    path('get/', views.session_get, name='session_get'),
    path('delete/', views.session_delete, name='session_delete'),
]
