from django.contrib.auth.models import User
from costaccouting.settings import AUTH_USER_MODEL
from yourcosts.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        person = User.objects.create_user(**validated_data)
        for i in Category.objects.filter(pk__lte=10):
            person.category.add(i)
        return person

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'balance']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name_cat']

class InfotmationTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfotmationTransaction
        fields = ['costs_sum', 'category', 'organization', 'description', 'user']
