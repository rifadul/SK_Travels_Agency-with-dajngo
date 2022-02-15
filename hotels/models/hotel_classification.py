from django.db import models

# Create your models here.
class Hotel_rating_in_star(models.Model):
    hotel_star = models.CharField(max_length=10, default='0')

    # tostring method overight
    def __str__(self):
        return self.hotel_star
