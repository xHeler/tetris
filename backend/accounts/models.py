from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars', null=True,
        default='avatar.jpg',
    )
    bio = models.TextField(max_length=150, blank=True)
