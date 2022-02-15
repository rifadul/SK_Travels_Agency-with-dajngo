from django.db import models

# Create your models here.
class Payment(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15)
    bank_card_name = models.CharField(max_length=30)
    bank_card_no = models.CharField(max_length=30)
    bank_card_expiration = models.CharField(max_length=30)
