from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactTemplateView, ProductDetailsView

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts_template"),
    path("product/<int:pk>/", ProductDetailsView.as_view(), name="product_detail")
]
