from django.views import generic
from .models import Book
from django.urls import reverse_lazy
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
    fields = ['title' , 'author' ,'translator','publishers' , 'description' ,'price' , 'cover' ]


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title' , 'author' ,'translator','publishers' , 'description' ,'price' , 'cover' ]
    # success_url = reverse_lazy('book_detail')

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
