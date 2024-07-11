from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Country, Leader

# Create your views here.

def home(request):
    #return render(request, 'home.html', {'title': 'Home'})
    return render(request, 'home.html')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    leaders = country.leader_set.all()
    return render(request, 'country_detail.html', {'country': country, 'leaders': leaders})

def leader_detail(request, pk):
    leader = get_object_or_404(Leader, pk=pk)
    return render(request, 'leader_detail.html', {'leader': leader})

def search_results(request):
    query = request.GET.get('q')
    results = Leader.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results':results , 'query':query})
