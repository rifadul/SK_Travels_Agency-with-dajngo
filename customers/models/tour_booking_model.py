from django.db import models

# Create your models here.
class Tour_booking(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=30,default='')
    email = models.EmailField(null=True)
    phoneNumber = models.CharField(max_length=15)
    tourist_place = models.CharField(max_length=50)
    pakage_price = models.IntegerField(max_length=15,default='0')
    number_of_adults = models.IntegerField(max_length=15,default='0')
    number_of_childen = models.IntegerField(max_length=15,default='0')
    payment_method  = models.CharField(max_length=15,default='')
    payment_mobile_number  = models.CharField(max_length=15)
    payment_transaction_number  = models.CharField(max_length=50)
    payment_amount = models.IntegerField(max_length=15)




    def register(self):
        self.save()