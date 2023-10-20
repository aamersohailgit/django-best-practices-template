from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)

class ModelFieldPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    can_access = models.BooleanField(default=True)
