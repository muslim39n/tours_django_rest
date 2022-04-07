from pyexpat import model
from rest_framework import serializers

from .models import Country, City

class CountrySerializerKz(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name_kz']

class CountrySerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name_ru']


class CitySerializerKz(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name_kz']
        
class CitySerializerRu(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name_ru']