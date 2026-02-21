from django.shortcuts import render
from rest_framework import viewsets
from .models import AcademicSession, School, Term
from .serializers import (
        AddSchoolSerializer,
        ViewSchoolSerializer,
        UpdateSchoolSerializer,
        SimpleSchoolSerializer,
        CreateSessionSerializer,
        ViewSessionSerializer,
        UpdateSessionSerializer,
        CreateTermSerializer,
        ViewTermSerializer,
        UpdateTermSerializer,
        GetCurrentTermSerializer
)
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_school(request):
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_all_schools(request):
    if request.user.role != 'super_admin':
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = ViewSchoolSerializer(schools, many=True)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_session(request):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'POST':
        serializer = CreateSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_sessions(request, school_id):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        sessions = AcademicSession.objects.filter(school__id=school_id)
        serializer = ViewSessionSerializer(sessions, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_term(request, school_id):
    if request.method == 'GET':
        try:
            term = Term.objects.get(school__id=school_id, is_current=True)
            serializer = GetCurrentTermSerializer(term)
            return Response(serializer.data)
        except Term.DoesNotExist:
            return Response({'error': 'Current term not found'}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_session(request, session_id):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    try:
        session = AcademicSession.objects.get(id=session_id)
    except AcademicSession.DoesNotExist:
        return Response({'error': 'Academic session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method in ['PUT', 'PATCH']:
        serializer = UpdateSessionSerializer(session, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_term(request):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'POST':
        serializer = CreateTermSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_terms(request, school_id):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        terms = Term.objects.filter(school__id=school_id)
        serializer = ViewTermSerializer(terms, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_term(request, term_id):
    if request.user.role != 'school_admin' or request.user.role != "super_admin":
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    try:
        term = Term.objects.get(id=term_id)
    except Term.DoesNotExist:
        return Response({'error': 'Term not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method in ['PUT', 'PATCH']:
        serializer = UpdateTermSerializer(term, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_term(request, school_id):
    if request.method == 'GET':
        try:
            term = Term.objects.get(school__id=school_id, is_current=True)
            serializer = GetCurrentTermSerializer(term)
            return Response(serializer.data)
        except Term.DoesNotExist:
            return Response({'error': 'Current term not found'}, status=status.HTTP_404_NOT_FOUND)
    