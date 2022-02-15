from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from customers.models.sign_up import Create_account
from django.views import View


class Sign_Up(View):
    def get(self, request):
        return render(request, 'create_account.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('fname')
        last_name = post_data.get('lname')
        email = post_data.get('email')
        phone_number = post_data.get('phoneNumber')
        username = post_data.get('username')
        password = post_data.get('password')

        error_message = None
        success_message = None

        # get form value
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number
        }

        # assign data in database variable
        save_account_info = Create_account(first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           phone=phone_number,
                                           username=username,
                                           password=password)

        # cheek username & email are exist or not in database
        isExistsUsername = save_account_info.isExistsUsername()
        isExistsEmail = save_account_info.isExistsEmail()

        def error_message_handling(message):
            error_message = message
            data = {
                'error_message': error_message,
                'values': value
            }
            return data

        if isExistsEmail:
            data = error_message_handling('Email is taken')
            return render(request, 'create_account.html', data)

        elif isExistsUsername:
            data = error_message_handling('Username is taken')
            return render(request, 'create_account.html', data)

        elif len(phone_number) < 11 or len(phone_number) > 11:
            data = error_message_handling('Invalid Phone Number.Use must 11 Number')
            return render(request, 'create_account.html', data)

        elif len(password) < 6:
            data = error_message_handling('Password must be use minimum 6 character')
            return render(request, 'create_account.html', data)

        if not isExistsUsername:
            # success_message = 'Account create successfully'
            # # save form data
            save_account_info.password = make_password(save_account_info.password)
            # save data in database
            save_account_info.register()
            return redirect('login')
        error_message = 'Try Again'
        return render(request, 'create_account.html', {'error_message': error_message})
