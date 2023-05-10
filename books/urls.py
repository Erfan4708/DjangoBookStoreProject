from django.urls import path

from .views import BookListView , BookDetailView , AddBook

urlpatterns = [
    path('' , BookListView.as_view() , name = 'book_list'),
    path('<int:pk>/' ,BookDetailView.as_view() , name = 'book_detail'),
    path('add/' , AddBook.as_view() , name = 'add_book'),
]