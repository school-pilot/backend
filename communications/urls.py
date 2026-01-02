from django.urls import path
from . import views

urlpatterns = [
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_read, name='mark_read'),
]
