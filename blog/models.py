from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок блога")
    slug = models.CharField(max_length=200, verbose_name="URL", blank=True, null=True)
    content = models.TextField(verbose_name="Содержание блога", blank=True, null=True)
    preview = models.ImageField(upload_to="blog/photo", verbose_name="Превью блога", blank=True, null=True)
    created_at = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    published = models.BooleanField(verbose_name="Признак публикации", default=True)
    count_views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def save(self, *args, **kwargs):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
