from django.db import models
from students import models as student_models
from schools import models as school_models
from academics import models as academic_models
from staffs import models as staff_models
from django.utils import timezone

# Create your models here.
class FeeCategory(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. Tuition, Library")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.school.name}"
class FeeStructure(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    classroom = models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    fee_category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
    amount = models.FloatField()
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fee_category.name} - {self.classroom.class_assigned.name} - {self.school.name}"

class Invoice(models.Model):
    STATUS = [
        ('paid', 'Paid'),
        ('partial', 'Partial'),
        ('unpaid', 'Unpaid')
    ]
    student = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS)
    issued_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} Invoice "
    
class Payment(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
        ('flutterwave', 'Flutterwave')
    ]
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    reference = models.CharField()
    paid_at = models.DateTimeField(default=timezone.now)
    confirmed_by = models.ForeignKey(staff_models.StaffProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment for {self.reference} {self.amount} confirmed by {self.confirmed_by}"
    
class OutstandingBalance(models.Model):
    student = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    balance_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Outstanding Balance for {self.student.user.get_full_name()}: {self.balance_amount}"
    