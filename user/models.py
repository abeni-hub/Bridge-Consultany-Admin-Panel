from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_admin_user:
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)