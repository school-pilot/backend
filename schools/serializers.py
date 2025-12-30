from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    School,
    AcademicSession
)

User = get_user_model()


class AddSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'name','logo','address','phone','email','registration_number','motto'
        ]

class ViewSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ['id', 'is_active', 'created_at', 'updated_at']
        
class UpdateSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'name','logo','address','phone','email','registration_number','motto'
        ]
        read_only_fields = ['is_active', 'created_at', 'updated_at']
        
class SimpleSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'logo']
        
class CreateSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['school','name','start_date','end_date','is_current']