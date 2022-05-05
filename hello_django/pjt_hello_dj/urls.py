"""pjt_hello_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  #Módulo Http Response incluído

def minha_view(request):     #Essa função não fica neste arquivo, está aqui somente por exemplo
    return HttpResponse('Hello Django')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', minha_view)
]


"""
Comentários sobre o arquivo urls.py
1 - A string do path nunca começa com barra /
2 - A função do path recebe um Http Request e envia um HTTP Response, necessita de um número mínimo
de parâmetros: uma string rota e uma função view.
3 - Para o path indicar a raíz do site utilize como rota aspas vazias, path('', minha_view).
4 - A cada Request do cliente o servidor responde con um código de status, para saber esses
códigos consulte o arquivo Codigo_de_Respostas_HTTP.pdf.
5 - No arquivo acima também estão descritos os métodos de requisição HTTP.
"""

