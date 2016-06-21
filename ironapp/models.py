from datetime import datetime

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    account = models.IntegerField()

class AcctBalance(models.Model):
    entry = models.IntegerField()
    credit = models.BooleanField(default=1)
    debit = models.BooleanField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
    account = models.ForeignKey(Customer)

    def __str__(self):
        return self.customer.name

