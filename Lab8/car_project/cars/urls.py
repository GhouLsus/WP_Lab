from django.urls import path
from .views import car_form

urlpatterns = [
    path('', car_form, name='car_form'),
]