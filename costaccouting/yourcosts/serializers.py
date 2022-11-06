from django.contrib.auth.models import User
from costaccouting.settings import AUTH_USER_MODEL

from yourcosts.models import *
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
