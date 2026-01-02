from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_timetable, name='create_timetable'),
    path('class/<int:class_id>/', views.class_timetable, name='class_timetable'),
    path('teacher/<int:teacher_id>/', views.teacher_timetable, name='teacher_timetable'),
]
