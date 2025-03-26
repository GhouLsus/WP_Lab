from django.urls import path
from .views import first_page, second_page

urlpatterns = [
    path('', first_page, name='first_page'),
    path('second/', second_page, name='second_page'),
]
