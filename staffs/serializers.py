from rest_framework import serializers
from .models import Teacher
from accounts.models import User


class TeacherListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'user_name', 'user_email', 'employee_id', 'qualification', 'specialization', 'created_at']


class TeacherDetailSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'user_details', 'employee_id', 'qualification', 'specialization', 'department', 'created_at', 'updated_at']

    def get_user_details(self, obj):
        return {
            'id': obj.user.id,
            'email': obj.user.email,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
        }


class TeacherCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'password', 'employee_id', 'qualification', 'specialization', 'department']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.pop('email'),
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            password=validated_data.pop('password'),
            username=validated_data.get('employee_id'),
            role='teacher'
        )
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['qualification', 'specialization', 'department']
