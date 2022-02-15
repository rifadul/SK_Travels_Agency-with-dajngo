from django.contrib import admin
from .models.destinations_place import Locations
from .models.destinations_details import Destinations_overview


# show data in table formate in admin panal

# ****for destination_place****
class Admin_destination_place(admin.ModelAdmin):
    list_display = ['tourist_place_locations']

#  *** for destinations_details ****
class Admin_destinations_details(admin.ModelAdmin):
    list_display = ['tourist_place_name','tour_sort_description','tour_description','tour_facility','tour_price','tour_pakage','tour_date','tour_image']

# Register your models here.
admin.site.register(Locations,Admin_destination_place)
admin.site.register(Destinations_overview,Admin_destinations_details)