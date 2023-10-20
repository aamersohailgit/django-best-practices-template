from django.contrib import admin
from .models import CustomUser, UserType, ModelFieldPermission

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Define the fields, list displays, etc.
    list_display = ['username', 'first_name', 'last_name', 'user_type']

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(ModelFieldPermission)
class ModelFieldPermissionAdmin(admin.ModelAdmin):
    pass

