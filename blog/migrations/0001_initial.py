# Generated by Django 5.0.6 on 2024-06-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=150, verbose_name="Заголовок блога"),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="URL"
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True, null=True, verbose_name="Содержание блога"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/photo",
                        verbose_name="Превью блога",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "count_views",
                    models.IntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]
