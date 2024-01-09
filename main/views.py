from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import (
    UserProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Skills
)
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        testimonial = Testimonial.objects.filter(is_active=True)
        skill = Skills.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_feature=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        context['testimonials'] = testimonial
        context['blog'] = blogs
        context['portfolio'] = portfolio
        context['skills'] = skill
        return context
    
class BlogView(generic.ListView):
    model = Blog
    template_name = 'main/blog.html'
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active= True)
    
    def get_context_data(self, *args, **kwargs):
            
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context["blogs"] = Blog.objects.all().filter(is_recent= True)
        
        return context
    
    
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog-detail.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context["blogs"] = Blog.objects.all().filter(is_recent= True)
        
        return context
    

    
class ContactView(generic.TemplateView):

    template_name = 'main/contact.html'
    