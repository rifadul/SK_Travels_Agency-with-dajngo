from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from customers.models.sign_up import Create_account
from django.views import View


class Login_page(View):
    def get(self, request):
        request.session.clear()
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Create_account.get_customer_by_username(username)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                print('login done')
                print(customer.first_name)
                # session work
                request.session['customer'] = customer.id
                request.session['customer_first_name'] = customer.first_name
                request.session['customer_last_name'] = customer.last_name
                request.session['customer_username'] = customer.username
                request.session['customer_email'] = customer.email
                request.session['customer_phone'] = customer.phone
                return redirect('index')
            else:
                error_meassage = 'Email & Password invalid..'
                return render(request, 'login.html', {'error_meassage': error_meassage})

        else:
            error_meassage = 'Email & Password invalid..'
        return render(request, 'login.html', {'error_meassage': error_meassage})


def logout(request):
    request.session.clear()
    return redirect('index')
