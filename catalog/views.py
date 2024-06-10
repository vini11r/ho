from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


# def home(requests):
#     catalog = Product.objects.all()
#     context = {"products": catalog}
#     return render(requests, "product_list.html", context)

class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts_template.html"


# def contacts(requests):
#     return render(requests, "contacts_template.html")

class ProductDetailsView(DetailView):
    model = Product

# def product_info(requests, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requests, 'product_detail.html', context)
