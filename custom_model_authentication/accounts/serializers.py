from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many = False)
    class Meta:
        model = UserProfile        
        fields = (
            'user',
            'profile_pic',
            'bio',
            'contact_info',
        )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        )

    # validation check
    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password == confirm_password:
            user = User(first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            return user
        else:
            raise serializers.ValidationError("Passwords do not match")
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)