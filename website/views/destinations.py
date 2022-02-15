from django.shortcuts import render
from tourist_place.models.destinations_details import Destinations_overview


def destinations(request):
    destinations_obj = Destinations_overview.objects.all()
    return render(request, 'destination.html', {'destinations_obj': destinations_obj})
