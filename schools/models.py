from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='school_profile', blank=True, null=True)
    name = models .CharField(max_length=100)
    logo = models.ImageField(upload_to='school_logos/')
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    registration_number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    motto = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        
        return self.name
    
    
class SchoolSettings(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE, related_name='settings')
    grading_system_type = models.CharField(max_length=50, choices=[('percentage', 'Percentage'), ('letter', 'Letter Grade'), ('gpa', 'GPA')], default='percentage')
    max_score = models.PositiveIntegerField(default=100)
    min_passing_score = models.PositiveIntegerField(default=50)
    attendance_required_percentage = models.PositiveIntegerField(default=75)
    allow_result_download = models.BooleanField(default=True)
    allow_parent_access = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Settings for {self.school.name}"

class AcademicSession(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='academic_sessions')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.school.name})"

class Term(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='terms')
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.academic_session.name}"

