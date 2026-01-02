from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def assessment_list(request):
    """Create or list assessments."""
    if request.method == 'POST' and request.user.role != 'admin':
        return Response({'error': 'Only admins can create assessments'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'assessments': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enter_scores(request):
    """Enter scores."""
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can enter scores'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Scores entered'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_score(request, score_id):
    """Update score."""
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can update scores'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Score updated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_results(request):
    """Class result view."""
    if request.user.role != 'admin':
        return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'results': []}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_results(request):
    """Approve results."""
    if request.user.role != 'admin':
        return Response({'error': 'Only admins can approve'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Results approved'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_results(request, student_id):
    """Student result."""
    if request.user.role not in ['admin', 'student']:
        return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'results': []}, status=status.HTTP_200_OK)
