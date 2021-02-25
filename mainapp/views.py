from django.shortcuts import render


# функции = вьюхи = контроллеры
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',

    }
    return render(request, 'mainapp/products.html', context)

#
# 'products': [
#     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
#     {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
#     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
#     {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
#     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
#     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00'},
# ],