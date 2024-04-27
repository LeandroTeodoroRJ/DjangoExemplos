from django.shortcuts import render
from .models import Book
from django.http import Http404

# Create your views here.
#def home(request):
#    return render(request, 'app_main/pages/home.html')     #Função para chamada de um arquivo html, note o caminho
                                                           #que tem como base a pasta template.

def index(request):
    books = Book.objects.all()
    return render(request, 'app_main/pages/index.html', {
        "books_template": books
    })

def book_detail(request, book_id):
    try:
        books = Book.objects.get(id=book_id)
    except:
        raise Http404()
    return render(request, 'app_main/pages/book_detail.html', {
        "books_template": books
    })
