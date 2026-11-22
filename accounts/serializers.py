from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    class Meta:
        model = CustomUser
        fields = ['username', 'password','password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Паролҳо мувофиқат намекунанд')
        return data


    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)