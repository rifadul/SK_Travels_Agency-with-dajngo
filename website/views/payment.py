from django.shortcuts import render


# **************** payment page *******************
def payment(request):
    return render(request, 'payment.html')
