from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherListSerializer, TeacherDetailSerializer, TeacherCreateSerializer, TeacherUpdateSerializer


def has_admin(user):
    return user.role == 'admin'


def has_admin_or_teacher(user):
    return user.role in ['admin', 'teacher']


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def teacher_list(request):
    """List or create teachers."""
    if request.method == 'GET':
        if not has_admin(request.user):
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        teachers = Teacher.objects.all()
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not has_admin(request.user):
            return Response({'error': 'Only admins can create teachers'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeacherCreateSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response(TeacherDetailSerializer(teacher).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def teacher_detail(request, teacher_id):
    """Get or update teacher details."""
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        if not has_admin(request.user):
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        if not has_admin(request.user):
            return Response({'error': 'Only admins can update teachers'}, status=status.HTTP_403_FORBIDDEN)
        serializer = TeacherUpdateSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(TeacherDetailSerializer(teacher).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_subjects(request, teacher_id):
    """Assign subjects to a teacher."""
    if not has_admin(request.user):
        return Response({'error': 'Only admins can assign subjects'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    
    subjects = request.data.get('subjects', [])
    if not subjects:
        return Response({'error': 'subjects list is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Placeholder for subject assignment logic
    return Response({'message': f'{len(subjects)} subjects assigned to teacher'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacher_classes(request, teacher_id):
    """View assigned classes for a teacher."""
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Only teacher can view own classes, admins can view any
    if request.user.role == 'teacher' and teacher.user != request.user:
        return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    
    # Placeholder for classes list
    return Response({'classes': [], 'message': 'No classes assigned yet'}, status=status.HTTP_200_OK)
