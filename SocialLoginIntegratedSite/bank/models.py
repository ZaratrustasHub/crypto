from django.db import models

class TransactionHistory(models.Model):
    #transactionID = models.AutoField()
    date = models.DateField(auto_now= False,auto_now_add= True)
    accnumberfrom = models.CharField(max_length=26)
    accnumberto = models.CharField(max_length=26)
    cash = models.FloatField()
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.accnumberfrom

class customer(models.Model):
    transactions = models.ForeignKey(TransactionHistory, null=True, blank=True)
    name = models.CharField(max_length=128)
    accnumber = models.CharField(max_length=26, unique=True) # , min_length=26,
    saldo = models.FloatField(default=100)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name 
