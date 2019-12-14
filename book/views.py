from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from author.models import Author
from django.contrib.auth.models import User

def about_book(request):
    return render(request, 'book/book.html')


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'user/home.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'book/home.html'  #<app>/<model>_<view_type>.html
    context_object_name = 'books'
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'genre', 'published', 'image','author','date_added']

    def form_valid(self, form):
        form.instance.book_creator = self.request.user
        return super().form_valid(form)



class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['name', 'genre', 'published', 'image','author','date_added']

    def form_valid(self, form):
        form.instance.book_creator = self.request.user
        return super().form_valid(form)


class AuthorBookListView(ListView):
    model = Book
    template_name = 'book/author_books.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(Author, username=self.kwargs.get('username'))
        return Book.objects.filter(author=user)