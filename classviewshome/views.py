from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import ArticleForm, BookForm, CustomUserCreationForm

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


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'classviewshome/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name =form.cleaned_data['full_name']
        user.birth_date =form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)