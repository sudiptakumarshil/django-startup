from django.db import models
from settings.roles.models import Roles
from django.contrib.auth.models import User


# Create your models here.


class RouteType(models.Model):
    name = models.CharField(max_length=50)


class Permissions(models.Model):
    role = models.OneToOneField(
        Roles, related_name="permissions", on_delete=models.CASCADE
    )
    group_name = models.CharField(max_length=100)
    route_name = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=False)
    admin = models.ForeignKey(
        User, related_name="admin_permissions", on_delete=models.CASCADE
    )
    route_type = models.ForeignKey(RouteType, on_delete=models.CASCADE)
