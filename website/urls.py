from django.urls import path
# from .views.home import index

from website.views import home, hotel, login, logout, payment, sign_up, contact_page, destinations, destinations_details_page,hotel_details_page,hotel_booking,tour_booking
from website.views.login import logout

urlpatterns = [
    path('', home.Index.as_view(), name='index'),
    path('tour_details<int:id>', destinations_details_page.details_page, name='details'),
    path('hotel_details<int:id>', hotel_details_page.hotel_details, name='hotel_details'),
    path('contact', contact_page.contact_page, name='contact'),
    path('login', login.Login_page.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('sign_up', sign_up.Sign_Up.as_view(), name='create_account'),
    path('destination', destinations.destinations, name='destinations'),
    path('hotel', hotel.hotel, name='hotel'),
    path('payment', payment.payment, name='payment'),
    # new
    # path('tour_book<int:id>', tour_booking.Tour_booking, name='tour_booking'),
    path('tour_book<int:id>', tour_booking.Tour_Booking_view.as_view(), name='tour_booking'),
    path('hotel_booking<int:id>', hotel_booking.Hotel_Booking_view.as_view(), name='hotel_booking'),
    # path('hotel_booking<int:id>', hotel_booking.hotel_booking, name='hotel_booking'),

]

# from django.urls import path
#
# # from .views import home
# from .views.home import Index
#
# urlpatterns = [
#     path('', Index.as_view(), name='index'),
# ]