from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import ArticleForm, BookForm

class HomeView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп. информация'
        return context

class ArticleListView(ListView):
    model = Article
    # template_name = 'classviewshome/blog.html'

class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'text']
    success_url = '/articles/'

class ArticleDelete(DeleteView):
    model = Article
    fields = ['title', 'text']
    success_url = '/articles/'



class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

def get_context_date(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['article_books'] = Book.objects.filter(article=self.object)
    return context

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'description', 'article']
    success_url = '/books/'

class BookDelete(DeleteView):
    model = Book
    fields = ['title', 'description', 'article']
    success_url = '/books/'