from django.contrib.auth.models import User
from django.db import models

from author.models import Author

class Situation(models.Model):
    name = models.CharField(
        "A short desciption of the situation where the phrase" +
        "may occur (eg. 'meeting')",
        max_length=255,
        unique=True
    )
    authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='situations',
        through='Connection_Author_Situation'
    )
    private = models.BooleanField(
        "Is the information about this situation private",
        default=False
    )
    allowedUsers = models.ManyToManyField(
        User, 
        blank=True,
        related_name='allowedSituations'
    )
    blockedUsers = models.ManyToManyField(
        User, 
        blank=True,
        related_name='blockedSituations'
    )
    def __unicode__(self):
        return "%s" % (self.name)


class Connection_Author_Situation(models.Model):
    author        = models.ForeignKey(Author)
    situation     = models.ForeignKey(Situation)
    strength      = models.DecimalField(max_digits=5, decimal_places=4, default=0.5)
    timesShown    = models.IntegerField()
    timesSelected = models.IntegerField()
    timesRemoved  = models.IntegerField()
    class Meta:
        unique_together = ('author', 'situation')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.author, self.situation)


