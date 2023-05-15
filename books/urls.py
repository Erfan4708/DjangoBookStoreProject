from django.urls import path

from .views import BookListView  , AddBook ,BookUpdateView , BookDeleteView , book_detail_view,CommentDeleteView

urlpatterns = [
    path('' , BookListView.as_view() , name = 'book_list'),
    path('<int:pk>/' ,book_detail_view , name = 'book_detail'),
    path('add/' , AddBook.as_view() , name = 'add_book'),
    path('<int:pk>/update/' , BookUpdateView.as_view() , name = 'book_update'),
    path('<int:pk>/delete/' , BookDeleteView.as_view() , name = 'book_delete'),
    path('<int:pk>/delete_comment/' , CommentDeleteView.as_view() , name = 'comment_delete'),
]