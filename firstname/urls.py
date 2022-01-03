from django.urls import path
from firstname.views import getToken, Map

app_name = 'surname'
urlpatterns = [
    path('getToken/' , getToken , name = 'getToken'),
    path('map/' , Map.as_view(), name='map'),
]