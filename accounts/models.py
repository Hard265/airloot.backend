from django.db import models
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    quota = models.IntegerField(default=1024 * 1024 * 1024 * 5)  # Default quota in GB

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
