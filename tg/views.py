from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from .models import TGPage, TGUser
from tours.models import Tour
from locations.models import City

from tours.serializers import TourShortSerializer

class NewTGUser(APIView):
    def post(self, request):
        try: 
            tg_id = request.POST['user_id']

        except:
            return Response(status=HTTP_404_NOT_FOUND)

        try:
            user = TGUser.objects.get(tg_id=tg_id)
        except:
            user = TGUser(tg_id = tg_id)
        
        if 'username' in request.POST:
            user.username = request.POST['username']

        if 'name' in request.POST:
            user.name = request.POST['name']

        if 'lastname' in request.POST:
            user.lastname = request.POST['lastname']

        if 'phone_number' in request.POST:
            user.phone_number = request.POST['phone_number']

        user.save()

        return Response(status=HTTP_201_CREATED)

class PrevNextPage(APIView):
    def get(self, request, prev_or_next):
        
        try:
            tguser = TGUser.objects.get(tg_id=request.GET['user'])
        except:
            return Response(status=HTTP_404_NOT_FOUND)

        tgpage = TGPage.objects.filter(user=tguser).order_by('-created').first()
        request.GET = request.GET.copy()
        request.GET['country'] = tgpage.country.name_ru

        if prev_or_next == 'next':
            page = tgpage.page + 1

        elif prev_or_next == 'prev':
            page = max(tgpage.page - 1, 0)

        else:
            page = tgpage.page
        
        if tgpage.from_city.name == 'Almaty': 
            all_pages = (Tour.from_almaty.filter(country__pk = tgpage.country.id).count() - 1) // 5
            page = min(all_pages, page)

            tours = Tour.from_almaty.filter(country__pk = tgpage.country.id)[page * 5:(page + 1) * 5]
            
        else:
            all_pages = (Tour.objects.filter(country__pk = tgpage.country.id).count() - 1) // 5
            page = min(all_pages, page)

            tours = Tour.objects.filter(country__pk = tgpage.country.id)[page * 5:(page + 1) * 5]

        if tguser is not None:
            tgpage_new = TGPage(user=tguser, from_city=tgpage.from_city, country=tgpage.country, page=page)
            tgpage_new.save()

        serializer = TourShortSerializer(tours, many=True)

        return Response({'page':page + 1, 'all_pages':all_pages + 1, 'data':serializer.data})