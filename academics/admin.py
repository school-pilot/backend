from django.contrib import admin
from academics import models as academic_models

# Register your models here.
@admin.register(academic_models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'school')
    search_fields = ('name', 'level')
    list_filter = ('school',)

@admin.register(academic_models.Arm)
class ArmAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name',)
    list_filter = ('school',)
    
@admin.register(academic_models.Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('class_assigned', 'arm', 'capacity', 'school')
    search_fields = ('class_assigned__name', 'arm__name')
    list_filter = ('school', 'class_assigned', 'arm')
    
@admin.register(academic_models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_core', 'school')
    search_fields = ('name', 'code')
    list_filter = ('school', 'is_core')
    
@admin.register(academic_models.SubjectAssignment)
class SubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'class_assigned', 'arm', 'teacher', 'session', 'school')
    search_fields = ('subject__name', 'class_assigned__name', 'arm__name', 'teacher__full_name')
    list_filter = ('school', 'session', 'class_assigned', 'arm')
    