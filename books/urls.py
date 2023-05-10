from django.urls import path

from .views import BookListView , BookDetailView , AddBook ,BookUpdateView , BookDeleteView

urlpatterns = [
    path('' , BookListView.as_view() , name = 'book_list'),
    path('<int:pk>/' ,BookDetailView.as_view() , name = 'book_detail'),
    path('add/' , AddBook.as_view() , name = 'add_book'),
    path('<int:pk>/update/' , BookUpdateView.as_view() , name = 'book_update'),
    path('<int:pk>/delete/' , BookDeleteView.as_view() , name = 'book_delete'),
]