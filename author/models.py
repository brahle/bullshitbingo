from django.contrib.auth.models import User
from django.db import models

from privacy.models import PrivacyControls

class Author(models.Model):
    GENDER_CHOICES = (
        ('U', 'Unknown'),
        ('M', 'Male'),
        ('F', 'Female')
    )

    firstName = models.CharField(
        "Author's first name", 
        blank=True, 
        max_length=255
    )
    lastName = models.CharField("Author's last name", max_length=255)
    gender = models.CharField(
        "Author's gender", 
        default='U',
        max_length=1, 
        choices=GENDER_CHOICES
    )
    privacyControls = models.OneToOneField(PrivacyControls)
    class Meta:
        unique_together = ('firstName', 'lastName')
    def __unicode__(self):
        return "%s %s" % (self.firstName, self.lastName);

