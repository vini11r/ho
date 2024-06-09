from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'objects_list'


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_create.html'
