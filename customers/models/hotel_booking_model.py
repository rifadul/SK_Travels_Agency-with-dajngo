from django.db import models

# Create your models here.
class Hotel_booking(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=30,default='')
    email = models.EmailField(null=True)
    phoneNumber = models.CharField(max_length=15)
    hotel_name  = models.CharField(max_length=50)
    # hotel_location = models.CharField(max_length=50)
    number_of_adults = models.IntegerField(max_length=15,default='0')
    number_of_childen = models.IntegerField(max_length=15,default='0')
    number_of_room = models.IntegerField(max_length=15,default='0')
    cheek_in_date = models.CharField(max_length=15,default='')
    cheek_in_out = models.CharField(max_length=15,default='')
    

    # def register(self):
    #     self.save()

    def register(self):
        self.save()