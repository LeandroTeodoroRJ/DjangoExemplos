# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from app_main import views      #Importação das funções da view do app

urlpatterns = [
    path('', views.starting_page, name="starting-page"),  #Carrega a função home que está dentro de view
    path('posts', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.post_detail, name="post-detail-page"),
]

"""
Comentários sobre o arquivo urls.py
1 - A string do path nunca começa com barra /
2 - Para utilizar um caminho da url do site faça path('pagina/', views.funcao),
que ficaria www.meusite.com/pagina/
3 - Para o path indicar a raíz do site utilize como rota aspas vazias, path('', minha_view).
4- Django official Documentation:
    slug - Matches any slug string consisting of ASCII letters or numbers,
    plus the hyphen and underscore characters. For example, building-your-1st-django-site.
    https://docs.djangoproject.com/en/3.1/topics/http/urls/#path-converters
"""
