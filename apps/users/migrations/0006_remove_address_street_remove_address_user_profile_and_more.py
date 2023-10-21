# Generated by Django 4.2.6 on 2023-10-21 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_family_name_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='address',
            name='landmark',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='street_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='unit_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_for', to='users.address'),
        ),
    ]
