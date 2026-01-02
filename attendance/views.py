from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request):
    """Mark attendance."""
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can mark attendance'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Attendance marked'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_attendance(request, attendance_id):
    """Update attendance."""
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can update attendance'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Attendance updated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_attendance(request):
    """View attendance."""
    if request.user.role not in ['admin', 'teacher']:
        return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'attendance': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_summary(request):
    """Attendance summary."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view summaries'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'summary': {}}, status=status.HTTP_200_OK)
