from django.urls import path

from .views import TourList, TourDetail

urlpatterns = [
    path('list/country/<int:country_id>/', TourList.as_view(), name='tour-short-list'),
    path('<int:tour_id>/', TourDetail.as_view(), name='tour-detail'),
]