from django.views.generic import ListView, DetailView
from .models import Category, Book

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(category_id=self.kwargs['pk'])

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'