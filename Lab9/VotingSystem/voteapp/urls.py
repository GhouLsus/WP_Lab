from django.urls import path
from .views import vote, results

urlpatterns = [
    path('', vote, name='vote'),
    path('results/', results, name='results'),
]
