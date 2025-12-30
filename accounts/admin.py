from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'last_login', 'date_joined')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    