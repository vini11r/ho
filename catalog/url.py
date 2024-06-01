from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info

app_name = CatalogConfig.name


urlpatterns = [
    path("", home, name="product_list"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product_info, name="product_info")
]
