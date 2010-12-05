from django.contrib.auth.models import User
from django.db import models

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
    private = models.BooleanField(
        "Is the information about this author private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name='allowedAuthors'
    )
    blockedUsers = models.ManyToManyField(
        User, 
        blank=True, 
        related_name='blockedAuthors'
    )
    class Meta:
        unique_together = ('firstName', 'lastName')
    def __unicode__(self):
        return "%s %s" % (self.firstName, self.lastName);

