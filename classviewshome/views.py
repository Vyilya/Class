from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class HomeView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп. информация'
        return context

class BlogView(ListView):
    model = Article
    # template_name = 'classviewshome/blog.html'