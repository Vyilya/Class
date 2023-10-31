from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('articles/', ArticleListView.as_view(), name = 'article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail'),
    path('create_article/', ArticleCreateView.as_view(), name = 'create_article'),
    path('books/', BookListView.as_view(), name = 'book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name = 'book_detail'),
    path('create_book/', BookCreateView.as_view(), name = 'create_book'),
    path('article/update/<int:pk>/', ArticleUpdate.as_view(),name='article_update'),
    path('article/delete/<int:pk>/', ArticleDelete.as_view(),name='article_delete'),
]