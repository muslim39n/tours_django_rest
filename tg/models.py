from email.policy import default
from django.db import models
from locations.models import Country, City
from datetime import datetime

class TGUser(models.Model):
    tg_id = models.IntegerField()
    username = models.CharField(max_length=64, blank=True, null=True, default="")
    name = models.CharField(max_length=64, blank=True, null=True, default="")
    lastname = models.CharField(max_length=64, blank=True, null=True, default="")
    phone_number = models.CharField(max_length=15, blank=True, default="")

class TGPage(models.Model):
    user = models.ForeignKey(TGUser, on_delete=models.CASCADE)
    from_city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    page = models.SmallIntegerField() #0-indexed
    created = models.DateTimeField(blank=True, default=datetime.now)
    
    

    