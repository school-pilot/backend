from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('<int:teacher_id>/assign-subjects/', views.assign_subjects, name='assign_subjects'),
    path('<int:teacher_id>/classes/', views.teacher_classes, name='teacher_classes'),
]
