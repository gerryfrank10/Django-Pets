from django.shortcuts import render
from .models import BookInstance, Book, Author, Genre


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all()
    

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances' : num_instances,
        'num_authors' : num_authors,
    }
    return render(request, 'index.html',context=context)
