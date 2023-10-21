# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  #
    bio = models.TextField(null=True, blank=True)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    pass  # For now, use the default fields provided by AbstractUser
