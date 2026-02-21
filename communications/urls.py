from django.urls import path
from . import views

urlpatterns = [
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('announcements/create/', views.create_announcement, name='create_announcement'),
    path('announcements/<int:announcement_id>/update/', views.update_announcement, name='update_announcement'),
    path('notifications/<int:notification_id>/read/', views.mark_read, name='mark_read'),
    
    path('notifications/create/', views.create_notification, name='create_notification'),
    path('notifications/<int:notification_id>/update/', views.update_notification, name='update_notification'),
]
