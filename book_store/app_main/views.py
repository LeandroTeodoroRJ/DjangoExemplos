from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.
#def home(request):
#    return render(request, 'app_main/pages/home.html')     #Função para chamada de um arquivo html, note o caminho
                                                           #que tem como base a pasta template.

def index(request):
    books = Book.objects.all().order_by("title")  #For discend order order_by("-title")
    num_boooks = books.count()  #Internal agregation method that it do to count registers
    anv_rating = books.aggregate(Avg("rating"))  #rating__avg, rating__avg_min, ...
    return render(request, 'app_main/pages/index.html', {
        "books_template": books,
        "total_number_of_books": num_boooks,
        "average_rating": anv_rating
    })

def book_detail(request, slug_book_name):
    try:
        books = Book.objects.get(slug=slug_book_name)
    except:
        raise Http404()
    return render(request, 'app_main/pages/book_detail.html', {
        "books_template": books
    })
