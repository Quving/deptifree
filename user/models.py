from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ApplicationUser(AbstractUser):

    username = models.CharField(default="", max_length=20, unique=True)
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
