from django.shortcuts import render,redirect
from django.views import View
from tourist_place.models.destinations_details import Destinations_overview
from hotels.models.hotel_list import Hotel_info


class Index(View):
    def get(self,request):

        # request.session.clear()

        destinations_obj = Destinations_overview.objects.all()
        hotel_obj = Hotel_info.objects.all()
        data = {
            'destinations_obj': destinations_obj,
            'hotel_obj': hotel_obj
        }

        print('Your id : ', request.session.get('customer'))
        print('first name : ', request.session.get('customer_first_name'))
        print('last name : ', request.session.get('customer_last_name'))
        print('Your username : ', request.session.get('customer_username'))
        print('Your email : ', request.session.get('customer_email'))
        print('Your phone : ', request.session.get('customer_phone'))
        # return render(request, 'index.html', {'destinations_obj': destinations_obj})
        print('reg ', request.GET)
        return render(request, 'index.html', data)

    # def post(self,request):
    #     selected_pakage = request.POST.get('plc_id')
    #     print("pakage", selected_pakage)

        # for cart
        # cart = request.session.get('cart')
        # if cart:
        #
        #     quantity = cart.get(selected_pakage)
        #
        #     if quantity:
        #         cart[selected_pakage] = quantity+1
        #     else:
        #         cart[selected_pakage] = 1
        #
        # else:
        #     cart = {}
        #     cart[selected_pakage] = 1

        # request.session['cart'] = cart
        # print('cart',request.session.get('cart'))
        # return redirect('destinations')

# def index(request):
#     # obj = Destinations_overview.objects.all()
#     destinations_obj = Destinations_overview.objects.all()
#     hotel_obj = Hotel_info.objects.all()
#     data = {
#         'destinations_obj': destinations_obj,
#         'hotel_obj': hotel_obj
#     }
#     print('Your id : ',request.session.get('customer_id'))
#     print('Your name : ',request.session.get('customer_first_name'))
#     print('Your username : ',request.session.get('customer_username'))
#     # return render(request, 'index.html', {'destinations_obj': destinations_obj})
#     return render(request, 'index.html', data)
