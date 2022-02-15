from django.shortcuts import render
from website.models.contact_form import Contact


def contact_page(request):
    if request.method == 'POST':
        contact = Contact()
        # get value from contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # insert value from database
        contact.name = name
        contact.email = email
        contact.message = message
        #     save data in database
        contact.save()

    return render(request, 'contact.html')
