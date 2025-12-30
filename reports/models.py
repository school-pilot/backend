from django.db import models
from schools import models as school_models
from academics import models as academic_models

# Create your models here.
class AttendanceReport(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    classroom =  models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Attendance Report for {self.classroom.class_assigned.name} - {self.term.name} {self.session.name}"
    
class PaymentReport(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    total_expected = models.FloatField()
    total_received = models.FloatField()
    total_pending = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment Report - {self.term.name} {self.session.name}"

class AcademicPerformanceReport(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    classroom =  models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    average_score = models.FloatField()
    highest_score = models.FloatField()
    lowest_score = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Academic Report for {self.classroom.class_assigned.name} - {self.term.name} {self.session.name}"