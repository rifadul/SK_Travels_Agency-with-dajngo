from django.db import models

# Create your models here.
class Create_account(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=1000)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Create_account.objects.get(username = username)
        except:
            return False


    def isExistsUsername(self):
        if Create_account.objects.filter(username = self.username):
            return True
        else:
            return False


    def isExistsEmail(self):
        if Create_account.objects.filter(email = self.email):
            return True
        else:
            return False



