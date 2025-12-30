from django.contrib import admin
from schools import models as school_models

# Register your models here.
@admin.register(school_models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'is_active', 'created_at')
    search_fields = ('name', 'registration_number', 'email', 'phone')
    list_filter = ('is_active',)
    ordering = ('-created_at',)

@admin.register(school_models.SchoolSettings)
class SchoolSettingsAdmin(admin.ModelAdmin):
    list_display = ('school', 'grading_system_type', 'max_score', 'min_passing_score', 'attendance_required_percentage', 'allow_result_download', 'allow_parent_access')
    search_fields = ('school__name',)
    list_filter = ('grading_system_type', 'allow_result_download', 'allow_parent_access')
    ordering = ('-created_at',)
    
@admin.register(school_models.AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'start_date', 'end_date', 'is_current')
    search_fields = ('name', 'school__name')
    list_filter = ('is_current',)
    ordering = ('-start_date',)
    
@admin.register(school_models.Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_session', 'school', 'start_date', 'end_date', 'is_current')
    search_fields = ('name', 'academic_session__name', 'school__name')
    list_filter = ('is_current',)
    ordering = ('-start_date',)

