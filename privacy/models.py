from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PrivacyControls(models.Model):
    private = models.BooleanField(
        "Is this information private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name='allowed'
    )
    blockedUsers = models.ManyToManyField(
        User, 
        blank=True, 
        related_name='blocked'
    )

