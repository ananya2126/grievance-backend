from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    village = models.CharField(max_length=100)
    role = models.CharField(max_length=10, default='user')

    def __str__(self):
        return self.username