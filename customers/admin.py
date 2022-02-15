from django.contrib import admin
from .models.sign_up import Create_account
from .models.payment import Payment
from .models.tour_booking_model import Tour_booking
from .models.hotel_booking_model import Hotel_booking

# show data in table formate in admin panal
class Admin_create_account(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','phone','username','password']

class Admin_payment(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','phone','bank_card_name','bank_card_no','bank_card_expiration']


class Admin_tour_book(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','phoneNumber','tourist_place','pakage_price','number_of_adults','number_of_childen','payment_method','payment_mobile_number','payment_transaction_number','payment_amount']

class Admin_hotel_book(admin.ModelAdmin):
    list_display  = ['first_name','last_name','email','phoneNumber','hotel_name','number_of_adults','number_of_childen','number_of_room','cheek_in_date','cheek_in_out']

# Register your models here.
admin.site.register(Create_account,Admin_create_account)
admin.site.register(Payment,Admin_payment)
admin.site.register(Tour_booking,Admin_tour_book)
admin.site.register(Hotel_booking,Admin_hotel_book)