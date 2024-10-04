from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=150)
    admin = models.ForeignKey(User, related_name='role_created_by', on_delete=models.CASCADE)
