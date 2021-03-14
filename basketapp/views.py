from django.shortcuts import render

from django.shortcuts import HttpResponseRedirect

from mainapp.models import Product
from basketapp.models import Basket


def basket_add(requst, product_id=None):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=requst.user, product=product)

    if not basket.exists():
        basket = Basket(user=requst.user, product=product)
        basket.quantity = 1
        basket.save()
        return HttpResponseRedirect(requst.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(requst.META.get('HTTP_REFERER'))