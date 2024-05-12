from django.contrib import admin
from django.urls import path 
from .views import BookListView,BookByAuthorView,BookBorrowView,BookReturnView,BookBorrowabilityView


urlpatterns = [
     path('books/', BookListView.as_view(), name='book-list'),
     path('books/author/<str:author_name>/',BookByAuthorView.as_view(), name= 'books-by-author'),
     path('books/<str:owl_id>/borrow/', BookBorrowView.as_view(), name='book-borrow'),
     path('books/<str:owl_id>/return/', BookReturnView.as_view(), name='book-return'),
     path('books/<str:owl_id>/borrowability/', BookBorrowabilityView.as_view(), name='book-borrowability'),


    
]
