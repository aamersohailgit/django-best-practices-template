from django.urls import path
from .views import (CustomObtainAuthToken, RegisterView, UserListCreateView,
    UserRetrieveUpdateDestroyView)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('login/', CustomObtainAuthToken.as_view(), name='api-token-auth'),
    path('register/', RegisterView.as_view(), name='register'),
]