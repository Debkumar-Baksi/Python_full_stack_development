from django.shortcuts import render, get_object_or_404,redirect
from .models import Book,Author
from django.views.generic import ListView, DetailView
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def books_by_author(request,author_id):
    author=get_object_or_404(Author,id=author_id)
    books=Book.objects.filter(author=author)
    context={'author':author,'books':books}
    return render(request,'library/book_by_author.html',context)

def add_book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'library/add_book.html',{'form':form})
    
    


class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'