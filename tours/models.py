from django.db import models
from locations.models import Country, City


'''
Tour:
    -id(pk)
    -title
    -description
    -country
    -from_city
    -price
    -date
    -days
    -services

    -travel_agency(none)
    -phone_number
    -telegram
    -delete_time    
    
Services:
    -id(pk)
    -name_kz
    -name_ru
    -description_kz
    -description_ru
'''

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='tours')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='tours')
    price = models.IntegerField()
    date = models.DateField()
    days = models.PositiveSmallIntegerField()
    services = models.ManyToManyField(Service, related_name='tours')

    travel_agency = models.CharField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15, blank=True, default='')
    telegram = models.CharField(max_length=32, blank=True, null=True, default=None)
    delete_time = models.DateTimeField(null=True, default=None)
    
    def __str__(self):
        return self.title[:50]