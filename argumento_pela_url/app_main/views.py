from django.shortcuts import render

# Create your views here.
def home(request, id):
    return render(request, 'app_main/pages/home.html', {'var': id})

    #Função para chamada de um arquivo html, o parâmetro 'id' passado na url é carregado
    #na variável dinâmica 'var' de home.html



