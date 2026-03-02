from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='sms_student_list'),
    path('add/', views.student_create, name='sms_student_create'),
    path('<int:pk>/edit/', views.student_update, name='sms_student_update'),
    path('<int:pk>/delete/', views.student_delete, name='sms_student_delete'),
]
