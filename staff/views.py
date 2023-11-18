from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from staff.models import Staff







# Create your views here.


#def login(request):
    #return render(request, "staff/login/login.html")  


def login(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        print(staff_id)
        print(user_email)
        print(user_password)
        
        try:
            staff = Staff.objects.get(staff_id=staff_id)
            if staff.email == user_email and staff.password == user_password:
                messages.success(request, 'Email and password are correct')
                if staff_id == '2':
                    return redirect('staff:manage')  # Перенаправление на страницу управления
                elif staff_id == '1':
                    return redirect('staff:admin')  # Перенаправление на страницу администратора
            else:
                messages.error(request, 'Email or password is incorrect')
        except Staff.DoesNotExist:
            messages.error(request, 'Staff ID does not exist')

    return render(request, 'staff/login/login.html')




def admin_panel(request):
    return render(request, 'staff/admin_pl.html')

def manage_panel(request):
    return render(request, 'staff/manage_pl.html')
