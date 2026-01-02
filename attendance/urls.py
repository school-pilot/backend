from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('<int:attendance_id>/', views.update_attendance, name='update_attendance'),
    path('', views.view_attendance, name='view_attendance'),
    path('summary/', views.attendance_summary, name='attendance_summary'),
]
