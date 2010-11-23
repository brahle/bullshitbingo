from django.contrib.auth.models import User
from django.db import models

from author.models import Author
from situation.models import Situation

class Phrase(models.Model):
    text = models.CharField(
        "The text of the phrase (eg. 'synergy')",
        max_length=255,
        unique=True
    )
    authors = models.ManyToManyField(
        Author, 
        blank=True,
        related_name='phrases',
        through='Connection_Author_Phrase'
    )
    situations = models.ManyToManyField(
        Situation,
        blank=True,
        related_name='phrases',
        through='Connection_Situation_Phrase'
    )
    private = models.BooleanField(
        "Is the information about this phrase private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name='allowedPhrases'
    )
    blockedUsers = models.ManyToManyField(
        User,
        blank=True,
        related_name='blockedPhrases'
    )
    def __unicode__(self):
        return "%s" % (self.text)


class Connection_Author_Phrase(models.Model):
    author        = models.ForeignKey(Author)
    phrase        = models.ForeignKey(Phrase)
    strength      = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        default=0.5
    )
    timesShown    = models.IntegerField()
    timesSelected = models.IntegerField()
    timesRemoved  = models.IntegerField()
    class Meta:
        unique_together = ('author', 'phrase')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.author, self.phrase)


class Connection_Situation_Phrase(models.Model):
    situation     = models.ForeignKey(Situation)
    phrase        = models.ForeignKey(Phrase)
    strength      = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        default=0.5
    )
    timesShown    = models.IntegerField()
    timesSelected = models.IntegerField()
    timesRemoved  = models.IntegerField()
    class Meta:
        unique_together = ('situation', 'phrase')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.situation, self.phrase)



