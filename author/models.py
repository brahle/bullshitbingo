from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Author(models.Model):
    firstName = models.CharField(
        "Author's first name", 
        blank=True, 
        max_length=255
    )
    lastName = models.CharField("Author's last name", max_length=255)
    gender = models.CharField(
        "Author's gender", 
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

