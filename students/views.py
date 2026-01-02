from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentListSerializer, StudentDetailSerializer, StudentCreateSerializer, StudentUpdateSerializer
import csv
from io import StringIO


def has_access(user, required_roles):
    """Check if user has required role."""
    return user.role in required_roles


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def student_list(request):
    """List students or create new student."""
    if request.method == 'GET':
        if not has_access(request.user, ['admin', 'teacher']):
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not has_access(request.user, ['admin']):
            return Response({'error': 'Only admins can create students'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(StudentDetailSerializer(student).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def student_detail(request, student_id):
    """Get, update, or deactivate a student."""
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        if not has_access(request.user, ['admin', 'teacher']):
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        if not has_access(request.user, ['admin']):
            return Response({'error': 'Only admins can update students'}, status=status.HTTP_403_FORBIDDEN)
        serializer = StudentUpdateSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(StudentDetailSerializer(student).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if not has_access(request.user, ['admin']):
            return Response({'error': 'Only admins can deactivate students'}, status=status.HTTP_403_FORBIDDEN)
        student.status = 'deactivated'
        student.save()
        return Response({'message': 'Student deactivated'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def promote_student(request, student_id):
    """Promote student to next class."""
    if not has_access(request.user, ['admin']):
        return Response({'error': 'Only admins can promote students'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    new_class = request.data.get('new_class')
    if not new_class:
        return Response({'error': 'new_class is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    student.current_class = new_class
    student.save()
    return Response({'message': f'Student promoted to {new_class}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_profile(request, student_id):
    """Get full student profile."""
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Student can view own profile, teachers and admins can view any
    if request.user.role == 'student' and student.user != request.user:
        return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = StudentDetailSerializer(student)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bulk_upload_students(request):
    """Bulk upload students via CSV."""
    if not has_access(request.user, ['admin']):
        return Response({'error': 'Only admins can upload students'}, status=status.HTTP_403_FORBIDDEN)
    
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8')
        reader = csv.DictReader(StringIO(decoded_file))
        
        created_count = 0
        errors = []
        
        for row_num, row in enumerate(reader, start=2):  # Start from 2 (header is row 1)
            try:
                serializer = StudentCreateSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
                    created_count += 1
                else:
                    errors.append(f'Row {row_num}: {serializer.errors}')
            except Exception as e:
                errors.append(f'Row {row_num}: {str(e)}')
        
        return Response({
            'message': f'{created_count} students created successfully',
            'created': created_count,
            'errors': errors
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
