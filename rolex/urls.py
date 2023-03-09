from rolex.views import *
from django.urls import path

app_name = "rolex_app"

urlpatterns = [
    path('dilli/', dilli, name='dilli'),
    path('muni/', muni, name='muni'),
]
