from django.views import generic
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def book_detail_view(request , pk):
    book = get_object_or_404(Book , pk=pk)
    book_comments = book.comments.all()
    return render(request , "books/book_detail.html" , {"book" : book , "comments" : book_comments})

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
