from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(null=True, blank=True)

    gender = models.CharField(choices=(('w', 'woman'), ('m', 'man'), ('n', 'not to say'),), null=False, blank=True,)
