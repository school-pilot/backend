from django.db import models
from schools.models import School

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=50, choices=[
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ])
    features = models.TextField()
    
    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.school.name} - {self.plan.name}"
    
class PaymentHistory(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('flutterwave', 'Flutterwave'),
    ])
    reference = models.CharField(max_length=100)
    paid_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.school.name} - {self.amount} on {self.paid_at.strftime('%Y-%m-%d')}"