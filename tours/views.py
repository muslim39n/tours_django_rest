from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from django.db.models import Q

from .models import Tour, Service
from locations.models import Country, City
from tg.models import TGUser, TGPage
from .serializers import TourShortSerializer, TourSerializer

class TourList(APIView):
    
    def get(self, request, city_name, format=None):
        #TG USER
        try:
            tguser = TGUser.objects.get(tg_id=request.GET['user'])
        except:
            tguser = None

        #COUNTRY
        try:
            country_name = request.GET['country']
            country = Country.objects.filter(Q(name_ru = country_name) | Q(name_kz = country_name)).first()

        except:
            return Response(status=HTTP_404_NOT_FOUND)
        
        #PAGE
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 0

        #CITY - TOURS
        if city_name == 'almaty':
            all_pages = (Tour.from_almaty.filter(country__pk = country.id).count() - 1) // 5
            page = min(all_pages, page)

            tours = Tour.from_almaty.filter(country__pk = country.id)[page * 5:(page + 1) * 5]
            city = City.objects.filter(name='Almaty').first()
            
        else:
            all_pages = (Tour.objects.filter(country__pk = country.id).count() - 1) // 5
            page = min(all_pages, page)

            tours = Tour.objects.filter(country__pk = country.id)[page * 5:(page + 1) * 5]
            city = City.objects.filter(name='Astana').first()

        if tguser is not None:
            tgpage = TGPage(user=tguser, from_city=city, country=country, page=page)
            tgpage.save()

        serializer = TourShortSerializer(tours, many=True)
        
        return Response({'page':page + 1, 'all_pages':all_pages + 1, 'data':serializer.data})


class TourDetail(APIView):

    def get(self, request, tour_id, format=None):
        try:
            tour = Tour.objects.get(pk=tour_id)
        except:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = TourSerializer(tour)

        return Response(serializer.data)
        