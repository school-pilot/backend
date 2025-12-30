from django.contrib import admin
from attendance import models as attendance_models
# Register your models here.
@admin.register(attendance_models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('school', 'classroom', 'date', 'term', 'marked_by', 'created_at')
    list_filter = ('school', 'classroom', 'date', 'term')
    search_fields = ('classroom__name', 'marked_by__full_name')
    
@admin.register(attendance_models.AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'student', 'status', 'remarks')
    list_filter = ('status',)
    search_fields = ('student__full_name', 'attendance__classroom__name')
    list_display_links = ('attendance', 'student')
