from yourcosts.models import *
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
