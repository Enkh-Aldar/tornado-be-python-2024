from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogsListView(ListView):
    model = Post
    template_name = "home.html"
    
class BlogsDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class BlogsCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    


class BlogsUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    
class BlogsDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")