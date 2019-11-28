from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Stock
from user.models import Order, Cart

cat = ['IoT', 'circuits', 'kits', 'mc', 'other']


# Index view.
def index(request):

    if 'cat' in request.GET:
        items = Stock.objects.filter(cat=request.GET['cat'])

    else:
        items = Stock.objects.all()
    items = list(items)
    for item in items:
        if item.quantity < 1:
            items.remove(item)
    return render(request, "sahara/index.html", {'items': items, "cat": cat})


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
                    item.quantity -= 1
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

    if request.method == "POST":
        cq = int(request.POST['qty'])
        order = Order.objects.filter(id=request.POST['order_id'])
        order = order[0]
        item = Stock.objects.filter(id=order.product.id)
        item = item[0]

        if item.quantity > cq > 1:
            shift = int(request.POST['qty']) - order.quantity
            order.quantity = int(request.POST['qty'])
            item.quantity -= shift
            order.save()
            item.save()

        else:
            cart = Cart.objects.filter(user=request.user)
            cart = cart[0]
            total = get_cart_total(cart)
            orders = cart.order_set.all()
            messages.error(request, f'not possible!')

            return render(request, "sahara/cart.html", {'cart': orders, 'total': total})

    cart = Cart.objects.filter(user=request.user)
    cart = cart[0]
    print(cart)
    total = get_cart_total(cart)
    orders = cart.order_set.all()
    return render(request, "sahara/cart.html", {'cart': orders, 'total': total})


def get_total(order):
    return order.quantity * order.product.cost


def get_cart_total(cart):
    orders = cart.order_set.all()
    total = 0
    for order in orders:
        total += get_total(order)

    return total


def bill(request):
    return render(request, 'sahara/bill.html')
