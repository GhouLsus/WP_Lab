from django.shortcuts import render

def car_form(request):
    manufacturers = {
        'Toyota': 'toyota.png',
        'Honda': 'honda.png',
        'Ford': 'ford.png',
        'BMW': 'bmw.png',
        'Mercedes': 'mercedes.png'
    }
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        image = manufacturers.get(manufacturer, '')
        return render(request, 'result.html', {'manufacturer': manufacturer, 'model': model, 'image': image})
    return render(request, 'car_form.html', {'manufacturers': manufacturers})
