from django.shortcuts import render
from rest_framework import viewsets
from .models import School
from .serializers import (
        AddSchoolSerializer,
        ViewSchoolSerializer,
        UpdateSchoolSerializer,
        SimpleSchoolSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_school(request):
    if request.user.role != 'super_admin':
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'POST':
        serializer = AddSchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_schools(request,school_id):
    if request.user.role != 'super_admin':
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        schools = School.objects.get(id=school_id)
        serializer = ViewSchoolSerializer(schools)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_school(request, school_id):
    if request.user.role != 'super_admin':
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method in ['PUT', 'PATCH']:
        serializer = UpdateSchoolSerializer(school, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
