from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_report(request):
    """Get attendance reports."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view attendance reports'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'report': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fees_report(request):
    """Get fees reports."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view fees reports'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'report': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def academics_report(request):
    """Get academics/results reports."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can view academics reports'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'report': []}, status=status.HTTP_200_OK)
