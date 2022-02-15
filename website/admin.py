from django.contrib import admin
from .models.contact_form import Contact



# show data in table formate in admin panal

# ****for contact form****
class Admin_contact_form(admin.ModelAdmin):
    list_display  = ['name','email','message']

    # ****for create account****
# class Admin_create_account(admin.ModelAdmin):
#     list_display  = ['first_name','last_name','email','phone_number','username','password']

# Register your models here.
admin.site.register(Contact,Admin_contact_form)