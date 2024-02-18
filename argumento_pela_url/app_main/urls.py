# ***** ARQUIVO DE URLS DO APP *****

from django.urls import path
from app_main import views      #Importação das funções da view do app

urlpatterns = [
    path('home/<id>', views.home),               #Carrega a função home que está dentro de view passando
                                                 #um argumento pela url do navegador
    path('somentenumeros/<int:id>', views.home), #Utilizando o path converter para aceitar somente
                                                 #números
]

"""
Comentários sobre o arquivo urls.py
1- Para executar a chamada ficaria http://127.0.0.1:8000/home/leandro
Sendo que 'leandro' é o argumento passado pela URL, aqui como <id>
2- Se o argumento passado estiver no meio da URL, antecedido por "/",
é necessário inserir a barra no path da forma:
path('home/<id>/', views.home),

Path converters¶
The following path converters are available by default:

str - Matches any non-empty string, excluding the path separator, '/'.
    This is the default if a converter isn’t included in the expression.
int - Matches zero or any positive integer. Returns an int.
slug - Matches any slug string consisting of ASCII letters or numbers,
    plus the hyphen and underscore characters. For example,
    building-your-1st-django-site.
uuid - Matches a formatted UUID. To prevent multiple URLs from mapping
    to the same page, dashes must be included and letters must be lowercase.
    For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
path - Matches any non-empty string, including the path separator, '/'.
    This allows you to match against a complete URL path rather than a
    segment of a URL path as with str.


"""
