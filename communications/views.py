from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    AnnouncementSerializer,
    NotificationSerializer,
    CreateAnnouncementSerializer,
    CreateNotificationSerializer,
    UpdateAnnouncementSerializer,
    UpdateNotificationSerializer,
    )
from communications.models import Announcement, Notification


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def announcement_list(request):
    """Create or list announcements."""
    if request.method == 'POST' and request.user.role != 'super_admin':
        return Response({'error': 'Only admins can create announcements'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'announcements': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_announcement(request):
    """Create a new announcement."""
    if request.user.role != 'super_admin':
        return Response({'error': 'Only admins can create announcements'}, status=status.HTTP_403_FORBIDDEN)
    serializer = CreateAnnouncementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_announcement(request, announcement_id):
    """Update an existing announcement."""
    if request.user.role != 'super_admin':
        return Response({'error': 'Only admins can update announcements'}, status=status.HTTP_403_FORBIDDEN)
    try:
        announcement = Announcement.objects.get(id=announcement_id)
    except Announcement.DoesNotExist:
        return Response({'error': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UpdateAnnouncementSerializer(announcement, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notifications(request):
    """Get user notifications."""
    notifications = Notification.objects.filter(user=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_notification(request):
    """Create a new notification."""
    if request.user.role not in ['super_admin', 'school_admin']:
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'POST':
        serializer = CreateNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_notification(request, notification_id):
    """Update an existing notification."""
    if request.user.role not in ['super_admin', 'school_admin']:
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UpdateNotificationSerializer(notification, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_read(request, notification_id):
    """Mark notification as read."""
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification marked as read'}, status=status.HTTP_200_OK)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found or access denied'}, status=status.HTTP_404_NOT_FOUND)