from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth Views
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('hello/', views.hello_world, name='hello_world'),

    # Function-based views for List and Detail
    path('', views.student_list, name='student_list'),
    path('<int:pk>/', views.student_detail, name='student_detail'),

    # Class-based views for Create, Update, Delete
    path('create/', views.StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
