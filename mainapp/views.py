from django.shortcuts import render
from mainapp.models import ProductCategory, Product


# функции = вьюхи = контроллеры
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'product_category': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

