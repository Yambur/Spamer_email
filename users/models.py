from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    first_name = models.CharField(max_length=50, verbose_name="имя")
    comment = models.TextField(verbose_name="комментарий", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

