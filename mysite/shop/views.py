from django.shortcuts import render
from .models import Stock


# Create your views here.
def index(request):
    items = Stock.objects.all()
    return render(request, "sahara/item.html", {'items': items})


def cart(request):
    return render(request, "sahara/cart.html")
