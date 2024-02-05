from django.urls import path
from .views import BlogsListView, BlogsDetailView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView

urlpatterns = [
    path("post/new/", BlogsCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogsDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogsUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogsDeleteView.as_view(), name="post_delete"),
    path("", BlogsListView.as_view(), name = "home"),
]