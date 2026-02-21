from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Notification, Announcement

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class CreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['user', 'message']
        extra_kwargs = {
            'user': {'write_only': True},
            'message': {'write_only': True},
        }
class UpdateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'is_read']
        read_only_fields = ['id', 'user', 'created_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']
        
class CreateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        extra_kwargs = {
            'title': {'write_only': True},
            'content': {'write_only': True},
        }

class UpdateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        read_only_fields = ['id', 'created_at']
        
