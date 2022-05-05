# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from app_main.views import home   #Uma importação de uma view deve ter seu caminho completo

urlpatterns = [
    path('', home),  #Home
]
