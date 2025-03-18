from django.contrib.auth.models import AbstractUser
from django.db import models
from .user_manager import CustomUserManager

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email






