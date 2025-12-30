from django.db import models
from students import models as student_models
from schools import models as school_models
from academics import models as academic_models

# Create your models here.
class Assessment(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="e.g. test, exam, quiz")
    max_score = models.FloatField()
    weight = models.FloatField(help_text="Weight of the assessment towards final grade (e.g. 0.4 for 40%)")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.school.name}"

class Score(models.Model):
    student = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(academic_models.Subject, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField()
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.full_name()} - {self.subject.name} - {self.assessment.name}: {self.score}"
    
class Result(models.Model):
    student = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    total_score = models.FloatField()
    average_score = models.FloatField()
    grade = models.CharField(max_length=2)
    remarks = models.TextField(blank=True, null=True)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Result for {self.student.full_name()} - {self.classroom.class_assigned.name} - {self.term.name} {self.session.name}"

class ReportApproval(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Report Approval for {self.result.student.full_name()} - Approved: {self.is_approved}"