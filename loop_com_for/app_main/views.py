from django.shortcuts import render

# Create your views here.
def home(request):
    nomes = ['Fulano', 'Beltrano', 'Ciclano']
    return render(request, 'app_main/pages/home.html', context={'var': nomes}) 

