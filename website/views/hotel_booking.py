from django.shortcuts import render, get_object_or_404
from hotels.models.hotel_list import Hotel_info
from customers.models.hotel_booking_model import Hotel_booking
from django.views import View

# correct
# def hotel_booking(request,id):
#     hotel_view_obj = get_object_or_404(Hotel_info, pk=id)
#     return render(request, 'hotel_booking.html',{'hotel_view_obj': hotel_view_obj})


# new

class Hotel_Booking_view(View):
    def get(self, request,id):
        hotel_view_obj = get_object_or_404(Hotel_info, pk=id)
        return render(request, 'hotel_booking.html',{'hotel_view_obj': hotel_view_obj})

    def post(self, request, id):
        # hotel_booking = Hotel_booking()
        # get value from contact form
        post_data = request.POST
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        email = post_data.get('email')
        phone_number = post_data.get('phoneNumber')
        hotel_name = post_data.get('hotel_name')
        number_of_adults = post_data.get('number_of_adults')
        number_of_childen = post_data.get('number_of_childen')
        number_of_room = post_data.get('number_of_room')
        cheek_in_date = post_data.get('cheek_in_date')
        cheek_in_out = post_data.get('cheek_in_out')

        # insert value
        # hotel_booking.first_name = first_name


        # print(first_name,last_name,email,phone_number,hotel_name,number_of_adults,number_of_childen,number_of_room,cheek_in_date,cheek_in_out)


        # assign data in database variable
        save_hotels_booking_details = Hotel_booking(first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           phoneNumber=phone_number,
                                           hotel_name=hotel_name,
                                           number_of_adults=number_of_adults,
                                           number_of_childen=number_of_childen,
                                           number_of_room=number_of_room,
                                           cheek_in_date=cheek_in_date,
                                           cheek_in_out=cheek_in_out,
                                           )

            # save data in database
        save_hotels_booking_details.register()
        success_message = 'Hotel Book successfully'
        return render(request, 'hotel_booking.html', {'success_message': success_message})