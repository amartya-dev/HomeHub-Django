from django.db import models
from django.contrib.auth.models import User


class Devices(models.Model):
    device_name = models.CharField(max_length=250)
    device_chip = models.CharField(max_length=20)
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
