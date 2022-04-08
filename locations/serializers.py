from pyexpat import model
from rest_framework import serializers

from .models import Country, City
from tours.models import Tour

class CountrySerializerKz(serializers.ModelSerializer):
    tours_count = serializers.SerializerMethodField('get_tour_count')

    class Meta:
        model = Country
        fields = ['id', 'name_kz', 'tours_count']

    def get_tour_count(self, obj):
        return Tour.objects.filter(country=obj).count()

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