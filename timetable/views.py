from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_timetable(request):
    """Create timetable."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can create timetables'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Timetable created'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_timetable(request, class_id):
    """Get class timetable."""
    return Response({'timetable': []}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacher_timetable(request, teacher_id):
    """Get teacher timetable."""
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can view timetables'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'timetable': []}, status=status.HTTP_200_OK)
