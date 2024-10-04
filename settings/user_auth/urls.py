from django.urls import path, include
from .views import user_register

urlpatterns = [
    # path("login/", hello_world, name="auth.login"),
    path("register/", user_register, name="auth.register"),
    # user_register
]
