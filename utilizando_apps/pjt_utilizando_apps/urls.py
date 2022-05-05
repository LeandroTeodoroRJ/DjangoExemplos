"""pjt_utilizando_apps URL Configuration

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
from django.urls import include     #Para inclusão de urls dentro do App

# As funções definidas aqui foram movidas para meu_app/views.py

urlpatterns = [
    path('admin/', admin.site.urls),     #O carregamento do módulo admin não é necessário.
    path('', include('meu_app.urls')),   #Observe a nota do django para orientações de como
                                         #como inserir uma urls com o include.
]

"""
É possível mover as urls de um App para um arquivo sem separado, a fim de manter a organização
do App. As urls comentadas foram movidas para o arquivo meu_app/urls.py, já que essas urls
pertencem ao App em questão.
A linha path já inlcui todas as urls filhas do App. Ou seja, as urls do App nesse caso foram
incluídas depois da raíz do site. Mas poderiam ser incluídas depois de um domínio qualquer,
por exemplo: path('form/', include('meu_app.urls')
"""
