from django.db import models
from accounts import models as accounts_models

# Create your models here.
BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Student(models.Model):
    user = models.OneToOneField(accounts_models.User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    admission_number = models.CharField(max_length=50, unique=True)
    admission_date = models.DateField()
    current_class = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('graduated', 'Graduated'), ('suspended', 'Suspended')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.admission_number}"
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    blood_group = models.CharField(max_length=5, blank=True, null=True, choices=BLOOD_GROUP_CHOICES)
    address = models.TextField()
    guardian = models.ForeignKey('Guardian', on_delete=models.SET_NULL, blank=True, null=True, related_name='student_profiles')
    
    def __str__(self):
        return f"Profile of {self.student.user.get_full_name()}"
    
class Guardian(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='guardians')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.relationship}) of {self.student.user.get_full_name()}"
    