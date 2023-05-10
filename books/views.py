from django.views import generic
from .models import Book
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class AddBook(generic.CreateView):
    model = Book
    template_name = 'books/add_book.html'
    fields = ['title' , 'author' , 'description' ,'price']

