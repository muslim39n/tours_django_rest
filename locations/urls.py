from django.urls import path

from .views import CountryList, CityList

urlpatterns = [
    path('countries/<str:lang>/', CountryList.as_view(), name='country-list'),
    path('cities/<str:lang>/', CityList.as_view(), name='city-list'),
]