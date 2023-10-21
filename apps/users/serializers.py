from rest_framework import serializers, exceptions
from .models import CustomUser, Tag, UserProfile, Address
from django.contrib.auth.models import Group
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'groups']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street_number', 'street_name', 'unit_number', 'city', 'state', 'postal_code', 'country', 'landmark')

class UserProfileSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)  # related to the UserProfile via 'addresses' related_name
    class Meta:
        model = UserProfile
        fields = ('full_name', 'family_name', 'phone_number', 'date_of_birth', 'gender', 'addresses', 'bio', 'profile_picture', 'social_media_links')  # added 'addresses'

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])  # Set a default value of empty list
        profile = UserProfile.objects.create(**validated_data)

        for address_data in addresses_data:
            Address.objects.create(user_profile=profile, **address_data)
        return profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'profile', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        try:
            profile_data = validated_data.pop('profile')
            groups_data = validated_data.pop('groups')
            password = validated_data.pop('password')
            
            full_name = profile_data.get('full_name', '')
            family_name = profile_data.get('family_name', '')
            
            # Split the full_name into first and last parts
            first_name = full_name.split(' ')[0] if full_name else ''
            last_name = family_name or ' '.join(full_name.split(' ')[1:])  # use family_name or the remaining parts of the full_name

            user = CustomUser(first_name=first_name, last_name=last_name, **validated_data)
            user.set_password(password)
            user.save()
            
            for group in groups_data:
                user.groups.add(group)
            
            # Create UserProfile and Address
            UserProfileSerializer().create({'user': user, **profile_data})
            
            return user
        except Exception as e:
            raise exceptions.ValidationError({"error": str(e)})


