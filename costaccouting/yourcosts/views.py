from django.db import transaction
from django.db.models import Count
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class UserRegister(APIView):
    """Регистрация пользователя"""
    def get(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"post": serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class DeleteCategory(APIView):
    """Удаление категории с личного кабинета"""
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not pk:
            return Response({"error": "not category"})
        try:
            name_cat_for_del = serializer.validated_data.get('name_cat')
            del_cat = Category.objects.get(name_cat=name_cat_for_del).pk
            User.objects.get(pk=pk).category.remove(del_cat)
        except:
            return Response({"error": "not category"})
        return Response({"your_category": CategorySerializer(User.objects.get(pk=pk).category.all(), many=True).data})


class ChangeCategory(APIView):
    """Добавление собственной категории пользователя"""
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_category = [i.name_cat for i in Category.objects.all()]
        if serializer.validated_data.get('name_cat') in list_category:
            return Response({"errors": "категория уже существует"})
        else:
            new_cat = Category.objects.create(name_cat=serializer.validated_data.get('name_cat'))
            User.objects.get(pk=pk).category.add(new_cat)
        return Response({"your_category": CategorySerializer(User.objects.get(pk=pk).category.all(), many=True).data})


class MyBalance(APIView):
    """Просмотр своего баланса"""
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        my_balance = User.objects.get(pk=pk)
        serializer = UserSerializer(my_balance)
        # count_tr = InfotmationTransaction.objects.values('user_id').annotate(Count('id'))
        # print(len(count_tr))
        return Response({"мой баланс": serializer.data['balance']})

    def put(self, request, **kwargs):
        pk = kwargs.get('pk')
        instance = User.objects.get(pk=pk)
        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"общий баланс": UserSerializer(instance).data['balance']})

class Transaction(APIView):
    """Проводим транзакции"""
    permission_classes = [IsAuthenticated]

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = InfotmationTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        added_instance = InfotmationTransaction.objects.create(**serializer.validated_data)
        t = InfotmationTransaction.objects.get(time_operation=added_instance.time_operation)
        t.user_id = pk
        t.save()
        h = User.objects.get(pk=pk).balance - serializer.validated_data.get('costs_sum')
        if h < 0:
            return Response({"errors": "недостаточно средств"})
        else:
            u = User.objects.get(pk=pk)
            u.balance = h
            u.save()
        return Response({"transaction":
                        InfotmationTransactionSerializer
                        (InfotmationTransaction.objects.filter(user_id=pk), many=True).data})
















