from django.shortcuts import render, get_object_or_404
from tourist_place.models.destinations_details import Destinations_overview
from customers.models.tour_booking_model import Tour_booking
from django.views import View

# def Tour_booking(request,id):
#     obj = get_object_or_404(Destinations_overview, pk=id)
#     return render(request, 'tour_booking.html',{'obj': obj})

class Tour_Booking_view(View):

    def get(self, request,id):
        obj = get_object_or_404(Destinations_overview, pk=id)
        return render(request, 'tour_booking.html',{'obj': obj})

    def post(self, request, id):
        post_data = request.POST
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        email = post_data.get('email')
        phone_number = post_data.get('phoneNumber')
        tourist_place = post_data.get('tourist_place')
        pakage_price = post_data.get('pakage_price')
        number_of_adults = post_data.get('number_of_adults')
        number_of_childen = post_data.get('number_of_childen')
        payment_method = post_data.get('payment_method')
        payment_mobile_number = post_data.get('payment_mobile_number')
        payment_transaction_number = post_data.get('payment_transaction_number')
        payment_amount = post_data.get('payment_amount')

        # insert value
        # hotel_booking.first_name = first_name


        # print(first_name,last_name,email,phone_number,hotel_name,number_of_adults,number_of_childen,number_of_room,cheek_in_date,cheek_in_out)


        # assign data in database variable
        save_tour_booking_details = Tour_booking(first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           phoneNumber=phone_number,
                                           tourist_place=tourist_place,
                                           pakage_price=pakage_price,
                                           number_of_adults=number_of_adults,
                                           number_of_childen=number_of_childen,
                                           payment_method=payment_method,
                                           payment_mobile_number=payment_mobile_number,
                                           payment_transaction_number=payment_transaction_number,
                                           payment_amount=payment_amount,
                                           )

            # save data in database
        save_tour_booking_details.register()
        success_message = 'Tour Book successfully'
        return render(request, 'tour_booking.html', {'success_message': success_message})  