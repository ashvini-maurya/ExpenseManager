from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    amount = models.FloatField()
    comment = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.category)