from django.db import models

'''
Country:
    - id(pk)
    - name
    - name_kz
    - name_ru

City:
    - id(pk)
    - name
    - name_kz
    - name_ru

'''

class Country(models.Model):
    name = models.CharField(max_length=40)
    name_kz = models.CharField(max_length=40)
    name_ru = models.CharField(max_length=40)

    def __str__(self):
        return self.name + ' <> ' +  self.name_kz

class City(models.Model):
    name = models.CharField(max_length=40)
    name_kz = models.CharField(max_length=40)
    name_ru = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name + ' <> ' + self.name_kz


