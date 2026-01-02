from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.class_list, name='class_list'),
    path('arms/', views.create_arm, name='create_arm'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/assign/', views.assign_subject, name='assign_subject'),
]
