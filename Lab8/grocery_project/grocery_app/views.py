from django.shortcuts import render
from .models import GroceryItem

def home(request):
    if not GroceryItem.objects.exists():
        GroceryItem.objects.bulk_create([
            GroceryItem(name="Wheat", price=40),
            GroceryItem(name="Jaggery", price=60),
            GroceryItem(name="Dal", price=80),
        ])

    groceries = GroceryItem.objects.all()
    return render(request, 'grocery_app/home.html', {'groceries': groceries})
