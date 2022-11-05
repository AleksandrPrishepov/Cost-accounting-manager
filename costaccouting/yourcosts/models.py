from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Добавляем в модель User поле 'баланс'"""
    balance = models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='баланс')

class InfotmationTransaction(models.Model):
    costs_sum = models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='cумма')
    time_operation = models.TimeField(auto_now_add=True,verbose_name='время')
    category = models.CharField(max_length=100, verbose_name='категория')
    organization = models.CharField(max_length=100, verbose_name='организация')
    description = models.TextField(max_length=250, verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')



