from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
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


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    # success_url = reverse_lazy('blog:blog_update')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_update', args=[self.kwargs.get('pk')])