from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(requests):
    catalog = Product.objects.all()
    context = {"products": catalog}
    return render(requests, "product_list.html", context)


def contacts(requests):
    return render(requests, "contacts.html")


def product_info(requests, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(requests, 'product_info.html', context)
