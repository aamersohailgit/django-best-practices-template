from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_updated_by")
    
    class Meta:
        abstract = True

class UserType(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Address(BaseModel):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name="addresses", null=True, blank=True)
    street_number = models.CharField(max_length=50, default='1')  
    street_name = models.CharField(max_length=50, blank=True, null=True)  
    unit_number = models.CharField(max_length=50, blank=True, null=True)  
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)  
    country = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)  
    
    def __str__(self):
        address_str = f"{self.street_number} {self.street_name}"
        if self.unit_number:
            address_str += f", {self.unit_number}"
        address_str += f", {self.city}, {self.state} {self.postal_code}, {self.country}"
        return address_str

class UserProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    primary_address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name="primary_for_users")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    social_media_links = models.JSONField(default=dict)  
    payment_method = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="user_profiles")
    default_address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name="default_for")
    
    def __str__(self):
        return self.user.username

class CustomUser(AbstractUser, BaseModel):
    pass  
