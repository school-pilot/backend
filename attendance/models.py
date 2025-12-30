from django.db import models
from schools import models as school_models
from academics import models as academic_models
from staffs import models as staff_models
from students import models as student_models

# Create your models here.
class Attendance(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    classroom = models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    marked_by = models.ForeignKey(staff_models.Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Attendance for {self.classroom.name} on {self.date}"

class AttendanceRecord(models.Model):
    attendance = models.ForeignKey(Attendance, related_name='records', on_delete=models.CASCADE)
    student = models.ForeignKey(student_models.Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')])
    remarks = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.student.full_name} - {self.status} on {self.attendance.date}"
    

    class Meta:
        unique_together = ('attendance', 'student')
