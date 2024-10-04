from django.db import models
from django.contrib.auth.models import User
from settings.roles.models import Roles


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, related_name="user_info", on_delete=models.CASCADE
    )
    roles = models.ManyToManyField(Roles, related_name="users")
    address = models.TextField()
    admin = models.ForeignKey(User, related_name="admin", on_delete=models.CASCADE)


class LoggedInUser(models.Model):
    user = models.ForeignKey(User, related_name="logged_user", on_delete=models.CASCADE)
    date = models.DateTimeField()
    device = models.TextField()
    session_key = models.CharField(max_length=40)
    location = models.CharField(null=True, max_length=150)
