from django.contrib.auth.models import User
from django.db import models

from author.models import Author
from connection.models import ConnectionDetails
from privacy.models import PrivacyControls

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
    def __unicode__(self):
        return "%s" % (self.name)

class Connection_Author_Situation(models.Model):
    author        = models.ForeignKey(Author)
    situation     = models.ForeignKey(Situation)
    connectionDetails = models.OneToOneField(ConnectionDetails)
    class Meta:
        unique_together = ('author', 'situation')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.author, self.situation)


