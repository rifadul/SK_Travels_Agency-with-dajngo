from django.shortcuts import render
from hotels.models.hotel_list import Hotel_info
from tourist_place.models.destinations_place import Locations


def hotel(request):
    hotel_obj = Hotel_info.objects.all()
    locations_obj = Locations.get_all_locations()
    data = {}
    data['hotel_obj'] = hotel_obj
    data['locations_obj'] = locations_obj

    return render(request, 'hotel.html', data)
