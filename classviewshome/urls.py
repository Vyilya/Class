from django.contrib.auth.views import LoginView, LogoutView
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
    path('book/update/<int:pk>/', BookUpdate.as_view(),name='book_update'),
    path('book/delete/<int:pk>/', BookDelete.as_view(),name='book_delete'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

]