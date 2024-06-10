from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="create"),
    path("", BlogListView.as_view(), name="list"),
]
