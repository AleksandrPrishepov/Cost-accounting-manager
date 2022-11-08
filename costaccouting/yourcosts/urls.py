from django.urls import path, include, re_path
from yourcosts.views import *


urlpatterns = [
    # path('login/', include('djoser.urls')),  # регестрация пользователя через djoser: http://127.0.0.1:8000/login/users/
    path('register/', UserRegister.as_view()), # регистрация пользователя через представление
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # авторизация пользователя по токену
    path('delete_your_cat/<int:pk>/', DeleteCategory.as_view()),  # удаление категории с личного кабинета
    path('new_cat/<int:pk>/', ChangeCategory.as_view()),  # добавление собственной категории пользователя
    path('my_balance/<int:pk>/', MyBalance.as_view()),  # просмотр своего баланса
    path('make_transaction/<int:pk>/', Transaction.as_view()),  # проводим транзакцию
]
