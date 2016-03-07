from django.db import models

# Create your models here.

class Transaction(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    def __unicode__(self):
        return self.category
