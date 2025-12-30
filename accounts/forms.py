from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'role', 'school', 'password1', 'password2']
        
        