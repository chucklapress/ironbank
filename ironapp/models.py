from datetime import datetime

from django.db import models

# Create your models here.


class AcctBalance(models.Model):
    entry = models.IntegerField()
    credit = models.BooleanField(default=1)
    debit = models.BooleanField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
    customer = models.ForeignKey('auth.User')
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name





