from django.db import models

# Create your models here.
class ConnectionDetails(models.Model):
    strength      = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        default=0.5
    )
    timesShown    = models.IntegerField(default=0)
    timesSelected = models.IntegerField(default=0)
    timesRemoved  = models.IntegerField(default=0)



