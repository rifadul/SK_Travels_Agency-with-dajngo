from django.shortcuts import render, get_object_or_404
from tourist_place.models.destinations_details import Destinations_overview


def details_page(request, id):
    obj = get_object_or_404(Destinations_overview, pk=id)
    return render(request, 'details.html', {'obj': obj})
