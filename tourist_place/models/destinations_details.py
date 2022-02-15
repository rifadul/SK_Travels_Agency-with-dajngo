from django.db import models
from .destinations_place import Locations


# Create your models here.
class Destinations_overview(models.Model):
    tourist_place_name = models.ForeignKey(Locations , on_delete=models.CASCADE , default='')
    tour_sort_description = models.CharField(max_length=200, default='')
    tour_description = models.TextField(max_length=1000, default='')
    tour_facility = models.TextField(max_length=1000, default='')
    tour_price = models.IntegerField(default=0)
    tour_pakage = models.CharField(max_length=100,default='')
    tour_date = models.CharField(max_length=100,default='')
    tour_image = models.ImageField(upload_to='upload/location_image/')