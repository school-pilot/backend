from django.db import models
from accounts.models import User
from schools.models import School

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    subject_specialization = models.CharField(max_length=100)
    date_hired = models.DateField()
    qualifications = models.TextField()
    is_active = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.staff_id}"
    
class StaffProfile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.staff.get_full_name()} - {self.position}"
    
    