from django.db import models

from author.models import Author
from connection.models import ConnectionDetails
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
    )
    def __unicode__(self):
        return "%s" % (self.text)


class Connection_Author_Phrase(models.Model):
    author            = models.ForeignKey(Author)
    phrase            = models.ForeignKey(Phrase)
    connectionDetails = models.OneToOneField(ConnectionDetails)
    class Meta:
        unique_together = ('author', 'phrase')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.author, self.phrase)


class Connection_Phrase_Situation(models.Model):
    situation         = models.ForeignKey(Situation)
    phrase            = models.ForeignKey(Phrase)
    connectionDetails = models.OneToOneField(ConnectionDetails)
    class Meta:
        unique_together = ('situation', 'phrase')
    def __unicode__(self):
        return "Connecting %s with %s" % (self.situation, self.phrase)


