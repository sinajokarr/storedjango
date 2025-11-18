from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   
    email = models.EmailField("email address", unique=True)

    phone = models.CharField(max_length=20, blank=True)
    is_marketing_opt_in = models.BooleanField(default=False)

    def __str__(self):
        return self.email or self.username
