from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def class_list(request):
    """List or create classes."""
    if request.method == 'POST' and request.user.role != 'admin':
        return Response({'error': 'Only admins can create classes'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'classes': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_arm(request):
    """Create class arm."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can create arms'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Arm created'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def subject_list(request):
    """List or create subjects."""
    if request.method == 'POST' and request.user.role != 'admin':
        return Response({'error': 'Only admins can create subjects'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'subjects': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_subject(request):
    """Assign subject."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can assign subjects'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Subject assigned'}, status=status.HTTP_200_OK)
