from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from django.db.models import Q

from .models import Tour, Service
from locations.models import Country
from .serializers import TourShortSerializer, TourSerializer

class TourList(APIView):
    
    def get(self, request, city_name, format=None):
        try:
            country_name = request.GET['country']
                
            country = Country.objects.filter(Q(name_ru = country_name) | Q(name_kz = country_name)).first()

        except:
            return Response(status=HTTP_404_NOT_FOUND)


        if city_name == 'almaty':
            tours = Tour.from_almaty.filter(country__pk = country.id)
        else:
            tours = Tour.objects.filter(country__pk = country.id)

        serializer = TourShortSerializer(tours, many=True)
        
        return Response(serializer.data)


class TourDetail(APIView):

    def get(self, request, tour_id, format=None):
        try:
            tour = Tour.objects.get(pk=tour_id)
        except:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = TourSerializer(tour)

        return Response(serializer.data)
        