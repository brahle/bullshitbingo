from django.db import models

from django.contrib.auth.models import User

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
        related_name="allowedAuthors"
    )
    blockedUsers = models.ManyToManyField(
        User, 
        blank=True, 
        related_name="blockedAuthors"
    )
    def __unicode__(self):
        return "%s %s" % (self.firstName, self.lastName);


class Situation(models.Model):
    name = models.CharField(
        "A short desciption of the situation where the phrase" +
        "may occur (eg. 'meeting')",
        max_length=255
    )
    private = models.BooleanField(
        "Is the information about this situation private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User, 
        blank=True,
        related_name="allowedSituations"
    )
    blockedUsers = models.ManyToManyField(
        User, 
        blank=True,
        related_name="blockedSituations"
    )
    def __unicode__(self):
        return "%s" % (self.name)
    

class Phrase(models.Model):
    text = models.CharField(
        "The text of the phrase (eg. 'synergy')",
        max_length=255
    )
    authors = models.ManyToManyField(Author, blank=True, related_name="phrases")
    situations = models.ManyToManyField(
        Situation,
        blank=True,
        related_name="phrases"
    )
    private = models.BooleanField(
        "Is the information about this phrase private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name="allowedPhrases"
    )
    blockedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name="blockedPhrases"
    )
    def __unicode__(self):
        return "%s" % (self.text)
