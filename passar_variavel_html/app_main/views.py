from django.shortcuts import render

# Create your views here.


def home(request):
    #Código da view aqui
    valor = 'TESTE'         #Valor da variável carregada para posterior render da página
    return render(request, 'app_main/home.html', {'var': valor})     #As variáveis são passadas como dicionário

#Também é possível fazer:
#    return render(request, 'app_main/home.html', context={'var': valor})  
