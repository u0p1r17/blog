from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.

from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields= [
        "title",
        "content",
    ]

@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = [
        "title",
        "content",
        "published",
    ]
    
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

    

@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url= reverse_lazy("posts:home")
    # template_name = "TEMPLATE_NAME"

