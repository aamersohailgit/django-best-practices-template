# users/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile, UserType, CustomUser

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'bio')
        
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    user_type = serializers.SlugRelatedField(queryset=UserType.objects.all(), slug_field='name', required=True)
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    # def create(self, validated_data):
    #     user = get_user_model().objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         first_name=validated_data.get('first_name', ''),
    #         last_name=validated_data.get('last_name', '')
    #     )
    #     return user
    def create(self, validated_data):
        user_type_data = validated_data.pop('user_type')
        user = CustomUser.objects.create_user(
            **validated_data
        )
        UserProfile.objects.create(user=user, user_type=user_type_data)
        return user
