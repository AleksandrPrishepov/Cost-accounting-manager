from django.urls import path, include, re_path
from yourcosts.views import UserRegister


urlpatterns = [
    # path('login/', include('djoser.urls')),  # регестрация пользователя через djoser: http://127.0.0.1:8000/login/users/
    path('register/', UserRegister.as_view()), # регистрация пользователя через представление
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # авторизация пользователя по токену

]
