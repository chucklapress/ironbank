from datetime import datetime

from django.db import models

# Create your models here.


class AcctBalance(models.Model):
    account_number = models.IntegerField()
    entry = models.DecimalField(max_digits=19, decimal_places=2)
    is_deposit = models.BooleanField(default=1)
    date = models.DateTimeField(default=datetime.now, blank=True)
    customer = models.ForeignKey('auth.User')
    memo_or_note = models.CharField(max_length=35)
    is_transfer = models.BooleanField(default=False)
    def __str__(self):
        return self.customer.username

class Transfer(models.Model):
    account_number = models.IntegerField()
    transfer_amount = models.DecimalField(max_digits=19, decimal_places=2)
    from_account = models.OneToOneField('auth.User')
    date =models.DateTimeField(default=datetime.now, blank=True)
    customer = models.ForeignKey(AcctBalance)
    memo_or_note = models.CharField(max_length=35)
    def __str__(self):
        return self.memo_or_note
