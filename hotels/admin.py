from django.contrib import admin
from .models.hotel_list import Hotel_info
from .models.hotel_classification import Hotel_rating_in_star

# show data in table formate in admin panal

# ****for contact form****
class Admin_Hotel_info(admin.ModelAdmin):
    list_display  = ['hotel_name','hotel_location','hotel_sort_description','hotel_description','hotel_facility','hotel_room_price','hotel_star','category_location','hotel_image']

class Admin_Hotel_rating_in_star(admin.ModelAdmin):
    list_display  = ['hotel_star']

# Register your models here.
admin.site.register(Hotel_info,Admin_Hotel_info)
admin.site.register(Hotel_rating_in_star,Admin_Hotel_rating_in_star)