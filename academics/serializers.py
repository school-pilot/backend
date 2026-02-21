from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Subject, Class, Arm, Classroom,Subject, SubjectAssignment

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class CreateSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'description']
        extra_kwargs = {
            'name': {'write_only': True},
            'code': {'write_only': True},
            'description': {'write_only': True},
        }
        
class UpdateSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'description']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class SubjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectAssignment
        fields = ['id', 'subject', 'teacher','class_assigned', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class CreateSubjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectAssignment
        fields = ['subject', 'teacher','class_assigned']
        extra_kwargs = {
            'subject': {'write_only': True},
            'teacher': {'write_only': True},
            'class_assigned': {'write_only': True},
        }

class UpdateSubjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectAssignment
        fields = ['subject', 'class_assigned']
        read_only_fields = ['id', 'teacher', 'created_at', 'updated_at']
        
class CreateArmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arm
        fields = ['name', 'school', 'description']
        extra_kwargs = {
            'name': {'write_only': True},
            'school': {'write_only': True},
            'description': {'write_only': True},
        }

class UpdateArmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arm
        fields = ['name', 'description']
        read_only_fields = ['id', 'school', 'created_at', 'updated_at']
        
class ArmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arm
        fields = ['id', 'name', 'school', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'school', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'school', 'description']
        extra_kwargs = {
            'name': {'write_only': True},
            'school': {'write_only': True},
            'description': {'write_only': True},
        }
        
class UpdateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'description']
        read_only_fields = ['id', 'school', 'created_at', 'updated_at']
        
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_assigned', 'arm', 'school', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class CreateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ...