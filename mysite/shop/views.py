from django.shortcuts import render, get_object_or_404
from .models import Stock
from django.contrib.auth.decorators import login_required
from user.models import Cart


# Create your views here.
def index(request):
    items = Stock.objects.all()
    return render(request, "sahara/index.html", {'items': items})


def item(request):
    return render(request, "sahara/item.html")


@login_required()
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0].products.all()
    print(cart)
    return render(request, "sahara/cart.html", {'cart': cart})
