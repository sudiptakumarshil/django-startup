from django.urls import path
from .views import StoreRoleView, RoleListView

urlpatterns = [
    path("create/", StoreRoleView.as_view(), name="roles.create"),
    path("index/", RoleListView.as_view(), name="roles.index"),
]
