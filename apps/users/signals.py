from django.db.models.signals import post_save
from django.apps import apps
from django.dispatch import receiver

def create_or_save_user_profile(sender, instance, created, **kwargs):
    UserProfile = apps.get_model('users', 'UserProfile')
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Then inside the ready() method in apps.py

def ready(self):
    from .models import CustomUser
    from . import signals

    post_save.connect(signals.create_or_save_user_profile, sender=CustomUser)
    post_save.connect(signals.save_user_profile, sender=CustomUser)
