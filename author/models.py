from django.contrib.auth.models import User
from django.db import models

from privacy.models import PrivacyControls

class Author(models.Model):
    GENDER_CHOICES = (
        ('U', 'Unknown'),
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(
        "Author's name", 
        blank=True, 
        max_length=255
    )
    nickname = models.CharField("Author's nickname", blank=True, max_length=255)
    gender = models.CharField(
        "Author's gender", 
        default='U',
        max_length=1, 
        choices=GENDER_CHOICES
    )
    
    class Meta:
        unique_together = ('name', 'nickname')
    def __unicode__(self):
        if self.nickname is None or self.nickname == '':
            return self.name
        return '{} ({})'.format(self.nickname, self.name);

