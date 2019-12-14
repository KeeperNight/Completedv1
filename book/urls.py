from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    AuthorBookListView
)
from . import views

urlpatterns = [
    path('', views.about_book, name="book"),
    path('home/', BookListView.as_view(), name="home"),
    path('author/<str:username>', AuthorBookListView.as_view(), name="author-book"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('new/', BookCreateView.as_view(), name="book-create"),
]
