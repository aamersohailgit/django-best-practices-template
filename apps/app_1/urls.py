from django.contrib import admin
from django.urls import path

from apps.app_1 import views

urlpatterns = [
    path("message/", views.message),
]
