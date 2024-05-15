# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from app_main import views      #Importação das funções da view do app

urlpatterns = [
    path('', views.ReviewView.as_view()),  #Carrega a função home que está dentro de view
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewListView.as_view()),
    path('reviews/<int:pk>', views.SingleReviewView.as_view()),
]

"""
Comentários sobre o arquivo urls.py
1 - A string do path nunca começa com barra /
2 - Para utilizar um caminho da url do site faça path('pagina/', views.funcao),
que ficaria www.meusite.com/pagina/
3 - Para o path indicar a raíz do site utilize como rota aspas vazias, path('', minha_view).

"""
