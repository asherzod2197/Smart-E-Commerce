from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError




class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        password1 = attrs['password']
        password2 = attrs['password2']

        if password1 != password2:
            raise ValidationError("Parollar bir hil emas.")
        return attrs



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'avatar']
        read_only_fields = ['id']

    












