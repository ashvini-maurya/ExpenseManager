from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#from datetime import datetime
import datetime
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s, %s, %s, %s, %s' % (self.amount, self.comment, self.category, self.user, self.created_at)



class Budget(models.Model):
    budget_amount = models.FloatField()
    user = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.budget_amount)