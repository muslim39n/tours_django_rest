from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Country, City
from .serializers import CountrySerializerKz, CountrySerializerRu, CitySerializerKz, CitySerializerRu

class CountryList(APIView):
    
    def get(self, request, lang, format=None):
        countries = Country.objects.all()

        if lang == 'kz':
            serializer = CountrySerializerKz(countries, many=True)
        elif lang == 'ru':
            serializer = CountrySerializerRu(countries, many=True)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)


class CityList(APIView):

    def get(self, request, lang, format=None):
        cities = City.objects.all()

        if lang == 'kz':
            serializer = CitySerializerKz(cities, many=True)
        elif lang == 'ru':
            serializer = CitySerializerRu(cities, many=True)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)