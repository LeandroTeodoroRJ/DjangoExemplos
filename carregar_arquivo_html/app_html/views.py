from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'app_html/home.html')     #Função para chamada de um arquivo html, note o caminho
                                                     #que tem como base a pasta template.


