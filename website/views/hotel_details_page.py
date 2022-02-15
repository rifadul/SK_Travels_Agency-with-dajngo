from django.shortcuts import render, get_object_or_404
from hotels.models.hotel_list import Hotel_info


def hotel_details (request, id):
    hotel_view_obj = get_object_or_404(Hotel_info, pk=id)
    return render(request, 'hotel_details.html', {'hotel_view_obj': hotel_view_obj})

