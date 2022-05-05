
# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from meu_app.views import home, sobre    #Uma importação de uma view deve ter seu caminho completo

urlpatterns = [
    path('', home),  #Home
    path('sobre/', sobre),  #Sub-domínio sobre apontando para a view sobre
]
