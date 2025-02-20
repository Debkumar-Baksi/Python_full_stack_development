from django.urls import path
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    # Function-based view URLs
    path("books/", views.book_list, name='book_list'),
    path('book/<str:book_id>/', views.book_details, name='book-details'),
    path('author/<str:author_id>/books',views.books_by_author,name='books_by_author'),
    path('books/add',views.add_book,name='add_book'),
    path('books/add_with_author/',views.add_book_and_author,name='add_book_and_author'),
    

    # Class-based view URLs
    # path("book-list/", BookListView.as_view(), name='book-list-view'),
    # path("book-detail/<int:pk>/", BookDetailView.as_view(), name='book-detail-view'),
]