from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    # path("login/", hello_world, name="auth.login"),
    path("register/", UserRegisterView.as_view(), name="auth.register"),
]
