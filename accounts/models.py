from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    telegram_username = models.CharField(max_length=150, null=True, blank=True)
    telegram_token = models.CharField(max_length=255, null=True, blank=True)
