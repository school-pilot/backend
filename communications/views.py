from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def announcement_list(request):
    """Create or list announcements."""
    if request.method == 'POST' and request.user.role != 'admin':
        return Response({'error': 'Only admins can create announcements'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'announcements': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notifications(request):
    """Get user notifications."""
    return Response({'notifications': []}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_read(request, notification_id):
    """Mark notification as read."""
    return Response({'message': 'Marked as read'}, status=status.HTTP_200_OK)
