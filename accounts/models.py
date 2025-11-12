from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_vendor=models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=False)
    address =models.TextField(blank=True)

