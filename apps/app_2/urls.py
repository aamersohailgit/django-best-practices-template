from django.contrib import admin
from django.urls import path, include

from apps.app_2 import views

urlpatterns = [
    path("message/", views.message),
]