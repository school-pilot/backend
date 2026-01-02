from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.attendance_report, name='attendance_report'),
    path('fees/', views.fees_report, name='fees_report'),
    path('academics/', views.academics_report, name='academics_report'),
]
