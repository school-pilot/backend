from django.db import models
from schools import models as school_models
from staffs import models as staff_models

# Create your models here.
class Class(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. Primary 1, JSS1")
    level = models.CharField(max_length=50, help_text="e.g. Primary, Junior Secondary")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Arm(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. A, B, Red House")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    arm = models.ForeignKey(Arm, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(help_text="Maximum number of students")
    
    def __str__(self):
        return f"{self.class_assigned.name} - {self.arm.name}"
    
class Subject(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. Mathematics, English")
    code = models.CharField(max_length=20, unique=True, help_text="e.g. MATH101")
    description = models.TextField(blank=True, null=True)
    is_core = models.BooleanField(default=False, help_text="Indicates if the subject is a core subject")

    def __str__(self):
        return self.name
    
class SubjectAssignment(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    # arm = models.ForeignKey(Arm, on_delete=models.CASCADE)
    teacher = models.ForeignKey(staff_models.Teacher, on_delete=models.CASCADE)
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subject.name} assigned to {self.class_assigned.name} - {self.teacher.full_name()} - {self.session.name}"
    
