from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(null=True, blank=True)

    gender = models.CharField(choices=(('w', 'woman'), ('m', 'man'), ('n', 'not to say'),), max_length=3, null=False, blank=True)
