#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Página Inicial')

def sobre(request):
    return HttpResponse('Página Sobre')

