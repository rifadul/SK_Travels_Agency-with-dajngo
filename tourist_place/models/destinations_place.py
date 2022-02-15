from django.db import models

# Create your models here.
class Locations(models.Model):
    tourist_place_locations = models.CharField(max_length=100,default='')

    @staticmethod
    def get_all_locations():
        return Locations.objects.all()

    # tostring method overight
    def __str__(self):
        return self.tourist_place_locations