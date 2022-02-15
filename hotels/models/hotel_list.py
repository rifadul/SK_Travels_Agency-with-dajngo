from django.db import models
from tourist_place.models.destinations_place import Locations
from .hotel_classification import Hotel_rating_in_star

# Create your models here.
class Hotel_info(models.Model):
    hotel_name = models.CharField(max_length=200, default='')
    hotel_location = models.CharField(max_length=100, default='')
    hotel_sort_description = models.CharField(max_length=100, default='')
    hotel_description = models.TextField(max_length=1000, default='')
    hotel_facility = models.TextField(max_length=1000, default='')
    hotel_room_price = models.IntegerField(default=0)
    hotel_star = models.ForeignKey(Hotel_rating_in_star , on_delete=models.CASCADE , default='')
    category_location = models.ForeignKey(Locations , on_delete=models.CASCADE , default='')
    hotel_image = models.ImageField(upload_to='upload/hotel_image/')



    @staticmethod
    def get_all_hotel():
        return Hotel_info.objects.all()

    @staticmethod
    def get_all_hotels_by_location_id(location_id):
        if location_id:
            return Hotel_info.objects.filter(location = location_id)
        else:
            return Hotel_info.get_all_hotel()


    # def get_absolute_url(self):
    #     return reverse("hotels:hotel_details_page", kwargs={"pk": self.pk})
    