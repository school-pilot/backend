from django.db import models
from students import models as student_models
from schools import models as school_models
from academics import models as academic_models
from accounts import models as account_models
from django.utils import timezone

TARGET_CHOICES = [
    ('all', 'All'),
    ('teachers', 'Teachers'),
    ('students', 'Students'),
    ('parents', 'Parents')
]

# Create your models here.
class Announcement(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    target = models.CharField(max_length=50, help_text="e.g. all, students, teachers", choices=TARGET_CHOICES)
    created_by = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Announcement: {self.title} \nCreated by {self.created_by}\nTarget: {self.target}"
    
class Notification(models.Model):
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Notification for {self.user.get_full_name()}: {self.message[:20]}..."
    

        