from django.contrib import admin
from students import models as students_models

# Register your models here.
@admin.register(students_models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'admission_number', 'school', 'current_class', 'status', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'admission_number', 'school', 'current_class')
    list_filter = ('status', 'school', 'current_class')
    ordering = ('-created_at',)
    
@admin.register(students_models.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'date_of_birth', 'gender', 'blood_group', 'guardian')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'guardian__name')
    list_filter = ('gender', 'blood_group')
    ordering = ('student__user__first_name',)
    
@admin.register(students_models.Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationship', 'student', 'contact_number', 'email')
    search_fields = ('name', 'student__user__first_name', 'student__user__last_name', 'relationship')
    ordering = ('name',)

