from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "slug", "content", "preview", "created_at", "published", "count_views"]
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog
    context_object_name = 'objects_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset
