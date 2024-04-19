from django.shortcuts import render

# Create your views here.
#def home(request):
#    return render(request, 'app_main/pages/home.html')     #Função para chamada de um arquivo html, note o caminho
                                                           #que tem como base a pasta template.

def starting_page(request):
    return render(request, 'app_main/pages/index.html')


def posts(request):
    return render(request, 'app_main/pages/home.html')

def post_detail(request):
    return render(request, 'app_main/pages/home.html')
