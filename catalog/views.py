from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


# def home(requests):
#     catalog = Product.objects.all()
#     context = {"products": catalog}
#     return render(requests, "product_list.html", context)

class ProductDetailsView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts_template.html"
# def contacts(requests):
#     return render(requests, "catalog/contacts_template.html")

# def product_info(requests, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requests, 'product_detail.html', context)
