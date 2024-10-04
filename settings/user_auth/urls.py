from django.urls import path, include
from .views import hello_world

urlpatterns = [
    path("login/", hello_world,name='auth.login'),

]
