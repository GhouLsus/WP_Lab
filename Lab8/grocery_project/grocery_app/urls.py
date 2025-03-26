from django.urls import path
from grocery_app.views import home

urlpatterns = [
    path('', home, name='home'),
]
