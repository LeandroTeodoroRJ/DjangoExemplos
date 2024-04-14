# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from app_main import views      #Importação das funções da view do app

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge-path")
]

"""
Comentários sobre o arquivo urls.py
1 - A string do path nunca começa com barra /
2 - Para utilizar um caminho da url do site faça path('pagina/', views.funcao),
que ficaria www.meusite.com/pagina/
3 - Para o path indicar a raíz do site utilize como rota aspas vazias, path('', minha_view).

"""
