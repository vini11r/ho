from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "slug", "content", "preview", "created_at", "published", "count_views"]
    success_url = reverse_lazy('catalog:product_list')
