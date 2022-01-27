from django.db import models

# Create your models here.


class asset_prices_model(models.Model):
    name        = models.CharField(max_length=30)
    code        = models.CharField(max_length=30)
    price       = models.FloatField()
    dateTime    = models.DateTimeField(auto_now=True)
    fiat_pair   = models.CharField(max_length=30)
    best_bid    = models.FloatField()
    best_ask    = models.FloatField()
    

    def __str__(self):
        return f"{self.code}{self.fiat_pair} price - {self.dateTime}"
