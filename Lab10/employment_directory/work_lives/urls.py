# work_lives/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_work/', views.add_work, name='add_work'),
    path('search_company/', views.search_company, name='search_company'),
]
