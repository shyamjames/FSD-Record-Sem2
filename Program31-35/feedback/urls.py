from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_feedback, name='submit_feedback'),
    path('list/', views.list_feedback, name='list_feedback'),
]
