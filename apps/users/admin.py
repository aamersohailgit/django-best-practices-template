# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, UserType, CustomUser
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_groups', 'bio')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groups'
    
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

