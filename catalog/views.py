from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
