from django.shortcuts import render

# Create your views here.
def home(request):
    var_view = True
    return render(request, 'app_main/pages/home.html', {'var':var_view})     #Função para chamada de um arquivo html, note o caminho
                                                                             #que tem como base a pasta template.

