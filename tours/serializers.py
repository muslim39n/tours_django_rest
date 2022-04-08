from rest_framework.serializers import ModelSerializer

from .models import Service, Tour

class TourShortSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'price', 'travel_agency']


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']


class TourSerializer(ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = ['id', 'title', 'description',
                'country', 'from_city', 'price',
                'date', 'days', 'travel_agency',
                'phone_number', 'phone_number_2', 'telegram',
                'services']


        '''
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
    '''