from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'all_posts'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'single_post'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')
