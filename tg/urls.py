from django.urls import path

from .views import NewTGUser, PrevNextPage

urlpatterns = [
    path('new_tg_user/', NewTGUser.as_view(), name='new-tg-user'),
    path('prev_next/<str:prev_or_next>', PrevNextPage.as_view(), name='prev-next')
]