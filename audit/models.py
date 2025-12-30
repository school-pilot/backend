from django.db import models
from accounts import models as account_models

# Create your models here.
class ActivityLog(models.Model):
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    model_affected = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.action} on {self.model_affected} at {self.timestamp}"
    
class LoginHistory(models.Model):
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"
    