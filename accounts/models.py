from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    # username = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

