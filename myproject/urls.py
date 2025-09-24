from django.urls import path
from books.views import (
    CategoryListView,
    BookListView, BookDetailView,
    AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('books/<int:pk>/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]