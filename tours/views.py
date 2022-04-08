from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import Tour, Service
from .serializers import TourShortSerializer, TourSerializer

class TourList(APIView):
    
    def get(self, request, city_name, country_id, format=None):
        if city_name == 'almaty':
            tours = Tour.from_almaty.filter(country__pk = country_id)
        else:
            tours = Tour.objects.filter(country__pk = country_id)
            
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
        