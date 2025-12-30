from django.db import models
from schools import models as school_models
from academics import models as academic_models
from staffs import models as staff_models

# Create your models here.
class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
    
class Timetable(models.Model):
    school = models.ForeignKey(school_models.School, on_delete=models.CASCADE)
    classroom = models.ForeignKey(academic_models.Classroom, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, help_text="e.g. Monday, Tuesday")
    session = models.ForeignKey(school_models.AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(school_models.Term, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Timetable for {self.classroom.class_assigned.name} - {self.day_of_week} - {self.session.name} {self.term.name}"
    
class TimetableEntry(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    subject = models.ForeignKey(academic_models.Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(staff_models.Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subject.name} by {self.teacher.full_name()} at {self.time_slot}"
    