from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.files.images import get_image_dimensions
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
   
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'email', 'bio']