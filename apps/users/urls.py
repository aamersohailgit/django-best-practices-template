from django.urls import path
from .views import (CustomObtainAuthToken, RegisterView, UserListCreateView,
    UserRetrieveUpdateDestroyView, UserRegistrationView, UserTypeListView, UserTypeDetailView)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('login/', CustomObtainAuthToken.as_view(), name='api-token-auth'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('user-types/', UserTypeListView.as_view(), name='user-type-list'),
    path('user-types/<int:pk>/', UserTypeDetailView.as_view(), name='user-type-detail'),
]