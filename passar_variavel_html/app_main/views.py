from django.shortcuts import render

# Create your views here.


def home(request):
    #Código da view aqui
    valor = 'TESTE'         #Valor da variável carregada para posterior render da página
    #As variáveis são passadas como dicionário
    return render(request, 'app_main/home.html', {'var': valor})

#Também é possível fazer:
#    return render(request, 'app_main/home.html', context={'var': valor})
