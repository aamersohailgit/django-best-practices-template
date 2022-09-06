from django.urls import path

from apps.app_3 import views

urlpatterns = [
    path("message/", views.message)
]