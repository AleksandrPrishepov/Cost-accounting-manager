from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Добавляем в модель User поле 'баланс'"""
    balance = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name='баланс')
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.username

class InfotmationTransaction(models.Model):
    """Данные по транзакции"""
    costs_sum = models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='cумма')
    time_operation = models.TimeField(auto_now_add=True,verbose_name='время')
    category = models.CharField(max_length=100, verbose_name='категория')
    organization = models.CharField(max_length=100, verbose_name='организация')
    description = models.TextField(max_length=250, verbose_name='описание')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.pk

class Category(models.Model):
    name_cat = models.CharField(max_length=100, verbose_name='название категории')
    # user_for_cat = models.ManyToManyField('User')

    def __str__(self):
        return self.name_cat

