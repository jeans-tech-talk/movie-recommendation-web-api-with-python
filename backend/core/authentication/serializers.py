from django.contrib.auth.models import User
from rest_framework import serializers


class UserWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        ]

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
