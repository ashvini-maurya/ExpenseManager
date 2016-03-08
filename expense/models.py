from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

class Transaction(models.Model):
    amount = models.FloatField()
    comment = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    user_id = models.IntegerField()

    def __unicode__(self):
        return self.category

class User(models.Model):
    user_id = models.ForeignKey(Transaction)


