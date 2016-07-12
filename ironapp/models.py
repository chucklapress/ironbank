from datetime import datetime

from django.db import models

# Create your models here.


class AcctBalance(models.Model):
    account_number = models.IntegerField()
    entry = models.IntegerField()
    is_deposit = models.BooleanField(default=1)
    date = models.DateTimeField(default=datetime.now, blank=True)
    customer = models.ForeignKey('auth.User')
    memo_or_note = models.CharField(max_length=35)
    def __str__(self):
        return self.name
