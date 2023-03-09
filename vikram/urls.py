from vikram.views import *
from django.urls import path

app_name="vikram_app"

urlpatterns = [
    path('first_vik', first_vik, name='first_vik'),

]
