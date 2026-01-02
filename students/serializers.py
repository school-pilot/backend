from rest_framework import serializers
from .models import Student, StudentProfile, Guardian
from accounts.models import User


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['id', 'name', 'relationship', 'contact_number', 'email', 'address']


class StudentProfileSerializer(serializers.ModelSerializer):
    guardian = GuardianSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'student', 'date_of_birth', 'gender', 'blood_group', 'address', 'guardian']


class StudentListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'user_name', 'user_email', 'admission_number', 'admission_date', 'current_class', 'status', 'created_at']


class StudentDetailSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    profile = StudentProfileSerializer(source='studentprofile', read_only=True)
    guardians = GuardianSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'user_details', 'school', 'admission_number', 'admission_date', 'current_class', 'status', 'profile', 'guardians', 'created_at', 'updated_at']

    def get_user_details(self, obj):
        return {
            'id': obj.user.id,
            'email': obj.user.email,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
        }


class StudentCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'password', 'school', 'admission_number', 'admission_date', 'current_class']

    def create(self, validated_data):
        # Create user
        user = User.objects.create_user(
            email=validated_data.pop('email'),
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.get('admission_number'),
            role='student'
        )
        # Create student
        student = Student.objects.create(user=user, **validated_data)
        return student


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['current_class', 'status', 'school']
