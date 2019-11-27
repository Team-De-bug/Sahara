from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Stock
from user.models import Order, Cart


# Index view.
def index(request):
    items = Stock.objects.all()
    return render(request, "sahara/index.html", {'items': items})


# Placing the order
@login_required()
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
                if item.quantity >= 1:
                    order.quantity += 1
                    item.quantity -=1
                    item.save()
                    order.save()
                break

        if not in_cart:
            if item.quantity >=1:
                order = Order(cart=user.cart, product=item)
                order.save()
                item.save()
                user.cart.order_set.add(order)
                item.quantity -= 1

    return HttpResponse("success")


# removing order from cart
@login_required()
def remove(request):

    if request.method == "GET":
        ID = request.GET['order_id']
        print(ID)
        order = Order.objects.filter(id=ID)
        order = order[0]
        item = Stock.objects.filter(id=order.product.id)
        item = item[0]
        item.quantity += order.quantity
        order.delete()
        item.save()

    return HttpResponse("success")


@login_required()
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0].order_set.all()
    print(cart)
    return render(request, "sahara/cart.html", {'cart': cart})
