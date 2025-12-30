from django.contrib import admin
from .models import Teacher, StaffProfile

# Register your models here.
# admin.site.register(Teacher)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'staff_id', 'school', 'subject_specialization', 'date_hired', 'is_active')
    search_fields = ('user__first_name', 'user__last_name', 'staff_id', 'subject_specialization')
    list_filter = ('school', 'is_active', 'date_hired')
    ordering = ('-date_hired',)

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'position', 'department')
    search_fields = ('staff__first_name', 'staff__last_name', 'position', 'department')