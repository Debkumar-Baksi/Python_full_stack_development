from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Book,Author
from django.views.generic import ListView, DetailView
from .forms import BookForm,AuthorForm
from .decorators import log_execution_time







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


@log_execution_time
@login_required
@permission_required('library.add_book',raise_exception=True)
def add_book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'library/add_book.html',{'form':form})


def add_book_and_author(request):
    if request.method=="POST":
        book_form=BookForm(request.POST)
        author_form=AuthorForm(request.POST)
        if book_form.is_valid() and author_form.is_valid():
            author=author_form.save()
            book=book_form.save(commit=False)
            book.author=author
            book.save()
            return redirect('book_list')
    else:
        book_form=BookForm()
        author_form=AuthorForm()
    return render(request,'library/add_book_and_author.html',
                      {'book_form':book_form,'author_form':author_form})
    
    


class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'