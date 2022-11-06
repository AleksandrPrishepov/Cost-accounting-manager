from django.shortcuts import render
from rest_framework.permissions import *
from costaccouting.settings import AUTH_USER_MODEL
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class UserRegister(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        # users = AUTH_USER_MODEL.objects.all()
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response({"post":serializer.data})

    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})



