from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from staff.models import Staff
from django.http import HttpResponseForbidden



# Create your views here.

#def login(request):
    #return render(request, "staff/login/login.html")  


def login(request):
    if request.method == 'POST':
        
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        
        print(user_email)
        print(user_password)
#проверяем, существует ли пользователь с таким email
        check_if_user_exists = Staff.objects.filter(email=user_email).exists()
#если пользователь существует, то продолжаем
        if check_if_user_exists:
            try:
# берём из БД юзера с указанным email
                staff=Staff.objects.get(email=user_email)             
# сверяем введённый пароль и хэшированный в БД
                if check_password(user_password, staff.password):
                    messages.success(request, 'Email and password are correct')

                    if staff.staff_id == 2:

                        return manage_panel(request)  # Перенаправление на страницу управления
                    elif staff.staff_id == 1:

                        return admin_panel(request)  # Перенаправление на страницу администратора
                else:
                    return render(request, 'staff/login/login_incorrect.html')
            except Staff.DoesNotExist:
                messages.error(request, 'Staff ID does not exist')
# если пользователя не существует в БД
        else:
            messages.error(request, 'Staff ID does not exist')

    return render(request, 'staff/login/login.html')




def admin_panel(request):
    if request.method == 'GET':
        return HttpResponseForbidden()  # возвращаем ошибку 403 
    return render(request, 'staff/admin_pl.html')


def manage_panel(request):
    if request.method == 'GET':
        return HttpResponseForbidden()  # возвращаем ошибку 403 
    return render(request, 'staff/manage_pl.html')