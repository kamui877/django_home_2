from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        page_number = request.GET.get('page', 1)
        reader = DictReader(file)
        paginator = Paginator([el for el in reader], 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
