from django.contrib import admin
from catalog.models import Category, Product, VersionProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(VersionProduct)
class VersionProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number_version", "name_version", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name_version", "number_version")

