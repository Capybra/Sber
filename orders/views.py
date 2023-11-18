from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages

from .models import OrderItem, Order
from cart.cart import Cart
from users.models import Profile 

import qrcode, random, string

def pin_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def pin_create(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        if len(phone) == 16:
            phone = phone.replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace('7', '', 1)
        try:
            profile = Profile.objects.get(phone=phone)
            if profile.user.username != '':
                profile.pincode = pin_generator()
                profile.save()
                response = {
                    'username': profile.name,
                    'pincode': profile.pincode
                }
        except:
            response = {'error': 'Пользователь не найден'}
    return JsonResponse(response)

def order_create(request):
    cart = Cart(request)
    qr_image = False
    if request.method == 'POST':
        phone = request.POST['phone']
        pincode = request.POST['pincode']
        if len(phone) == 16:
            phone = phone.replace('+', '').replace('(', '').replace(')', '').replace('-', '').replace('7', '', 1)
        try:
            profile = Profile.objects.get(phone=phone)
            if pincode != profile.pincode:
                response = {'pincodeerr': 'Не корректный ПИН-Код'}
                return JsonResponse(response)
            else:
                order = Order.objects.create()
                order.owner = profile
                order.save()
                profile.rating += 1
                profile.pincode = ''
                profile.save()
                data = {}
                for item in cart:
                    OrderItem.objects.create(
                        order = order,
                        product = item['product'],
                        price = item['price'],
                        quantity = item['quantity']
                    )
                    data['order'] = order
                    data['product'] = item['product']
                    data['price'] = item['price']
                    data['quantity'] = item['quantity']
                img = qrcode.make(data)
                img.save("media/qr/" + str(order.id) + ".png")
                qr_image = True
                cart.clear()
                send_mail(
                    'Заказ Оформлен', 
                    'Войдите в админ панель, что бы просмотреть новый заказ.' , 
                    'info@it-cube.krk', 
                    ['manager@it-cube.krk'], 
                    fail_silently=False
                )
                response = {
                    'username': profile.name,
                    'userrating': profile.rating,
                    'orderid': order.id
                }
                return JsonResponse(response)
        except:
            response = {'usernameerr': 'Пользователь не найден'}
            return JsonResponse(response)
    else:
        return render(request, 'orders/order/create.html')

