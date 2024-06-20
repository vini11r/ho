from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("", BlogListView.as_view(), name="blog_list"),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
]
