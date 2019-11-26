from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Stock
from user.models import Order, Cart

# Create your views here.
def index(request):
    items = Stock.objects.all()
    return render(request, "sahara/index.html", {'items': items})


def place(request):

    if request.method == "GET":
        ID = request.GET['product_id']
        item = Stock.objects.filter(id=ID)
        item = item[0]
        user = User.objects.filter(username=request.user)
        user = user[0]
        orders = user.cart.order_set.all()
        in_cart = False
        for order in orders:
            if item == order.product:
                print("in cart")
                in_cart = True
                order.quantity += 1
                order.save()
                break

        if not in_cart:
            order = Order(cart=user.cart, product=item)
            order.save()
            user.cart.order_set.add(order)
        #user.save()
    return HttpResponse("success")


def remove(request):

    if request.method == "GET":
        ID = request.GET['order_id']
        print(ID)
        order = Order.objects.filter(id=ID)
        order = order[0]
        order.delete()

    return HttpResponse("success")


@login_required()
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0].order_set.all()
    print(cart)
    return render(request, "sahara/cart.html", {'cart': cart})
