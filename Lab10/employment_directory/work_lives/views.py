# work_lives/views.py
from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, CompanySearchForm

def index(request):
    return render(request, 'work_lives/index.html')

def add_work(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorksForm()
    return render(request, 'work_lives/add_work.html', {'form': form})

def search_company(request):
    results = []
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            results = Works.objects.filter(company_name=company_name).select_related()
            results = [
                {
                    'person_name': work.person_name,
                    'city': Lives.objects.filter(person_name=work.person_name).first().city
                }
                for work in results
            ]
    else:
        form = CompanySearchForm()
    return render(request, 'work_lives/search_company.html', {'form': form, 'results': results})
