# PROJETO DJANGO.
## INSTALAÇÃO E CONFIGURAÇÃO DO AMBIENTE
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install git curl build-essential dkms perl wget -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
  libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pip setuptools wheel --upgrade
pip3 nstall django
pip3 install pytest
deactivate
```

## VERSÕES
Python: 3.10.12
Django Framework: 5.0.1


## ORDEM SUGERIDA DE LEITURA DOS PROJETOS.
hello_django  ::  Primeiro exemplo no framework Django. Entendendo o arquivo urls.py.\
boillerplate  ::  Escrevendo uma estrutura básica de projetos Django.\
utilizando_apps  ::  Iniciando um novo App e entendendo a sua estrutura de arquivos. \
carregar_arquivo_html  :: Como carregar um arquivo html utilizando o render e namespace. \
passar_variavel_html  ::  Passando uma variável do python para dentro do html. \
arquivo_parcial_html  \
arquivos_estaticos  

OBS: Ler o arquivo 'objetivos.txt' de cada projeto para um resumo dos
tópicos de cada exemplo.

## ROTEIRO CRIAÇÃO DE PROJETO
1 - Criar a pasta do projeto e a máquina virtual.\
2 - django-admin startproject <nome_projeto> . (Cria o projeto na pasta atual ".")\
3 - python manage.py startapp. (Para criar um App)\
4 - Editar seetings.py em installed_apps. \
5 - Criar a pasta templates/app_<nome> dentro do app principal.\
6 - Criar o home.html \
7 - Criar arquivo app/urls.py \
8 - Editar arquivo app/views.py \
9 - Checar com startrunserver ($python3 manage.py runserver)(Servidor rodando no endereço http://127.0.0.1:8000/)

## ESTRUTURAS DE ARQUIVO DO PROJETO DJANGO
```
\Pasta Inicial
    db.sqlite3 - Arquivo de banco de dados do sqlite3
    manage.py - Arquivo que tem a mesma função do comando djando-admin,
                antes da execução do manage.py ele carrega as configurações
                do arquivo settings.py
    \.mypy_cache - Arquivos de cache do plug-in MyPy do VS code
    \Nome Projeto - Pasta do projeto iniciado com startproject do django
        \__pychache__ - Pasta de cache do python
        urls.py - Arquivo que importas as funções das views e interliga ao domínio url do App.
        __init__.py - Indica que a pasta atual é um pacote do python. Pode ser usado para inicializar o pacote.
        asgi.py - Utilizado em produção para fazer a ligação e o servidor Web.
        wsgi.py - Utilizado em produção para fazer a ligação e o servidor Web.
        settings.py - Possui diversas configurações do django.
    \App - Pasta do App
        __init__.py - Arquivo de indicação de pacote.
        apps.py - Nome do App
        admin.py - Registro de modelos.
        models.py - Arquivo de criação de modelos.
        urls.py - Arquivo de rotas do App, aponta para as views do App.
        viwes.py - Arquivo de renderização das páginas (views).
        tests.py - Arquivo de testes.
        \migrations - Pasta de migrações da base de dados
        \template - Pasta com templates html (utilizar namespace)
            \App - Pasta namespace.
                \pages - Pasta de arquivos html do App
                    home.thml - Exemplo de uma página html do pertencente ao App.
    \venv - Pasta da máquina virtual do python
        \bin
            activate - Script de ativação da máquina virtual do python

>> <static> - Pasta com os arquivos estáticos do App (utilizar namespace)
>>> <partials> - Pasta com códigos parciais html
>>> <pages> - Pasta com as páginas html
> <base_static/global> - Pasta com os tipos de arquivos estáticos globais
> <base_templates/global> - Pasta com os tipos de arquivos templates globais
```

## LINKS ÚTEIS
Códigos de status de respostas HTTP: [MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status).\
Métodos de requisição HTTP[MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods).
