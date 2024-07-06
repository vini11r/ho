
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="catalog/photo", verbose_name="Превью продукта", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена продукта")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)
    updated_at = models.DateField(verbose_name="Дата изменения", auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    publisher = models.BooleanField(default=False, verbose_name="Опубликовать")

    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)
        permissions = [
            ('is_published', 'Подтверждает публикацию'),
            ('is_description', 'Может менять описание'),
            ('is_category', 'Может менять категорию')
        ]

    def __str__(self):
        return self.name


class VersionProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    number_version = models.SmallIntegerField(default=0, verbose_name="Версия продукта")
    name_version = models.CharField(max_length=200, verbose_name="Название версии", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Версия активна")

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ("number_version",)

    def __str__(self):
        return f"{self.name_version} - {self.number_version}"
