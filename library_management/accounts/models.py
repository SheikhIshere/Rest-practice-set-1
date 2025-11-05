from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from .manager import UserManager

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    

    # for admin use
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # when to keep it filled or when to make it empty

    def __str__(self):
        return self.username