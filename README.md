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
pip freeze > requirements.txt       (export requirements)
pip install -r requirements.txt     (when create a new VM)
```

## VERSÕES
Python: 3.10.12
Django Framework: 5.0.1

## ARQUIVOS EM ANEXO
requirements.txt  ::  Arquivo de dependências para a máquina virtual. \
Codigos_de_respostas_HTTP.pdf  ::  Respostas do protocolo http. \


## ORDEM SUGERIDA DE LEITURA DOS PROJETOS.
hello_django  ::  Primeiro exemplo no framework Django. Entendendo o arquivo urls.py.\
boillerplate  ::  Escrevendo uma estrutura básica de projetos Django.\
boillerplate_simple  ::  Estrutura básica sem arquivos globais. \
utilizando_apps  ::  Iniciando um novo App e entendendo a sua estrutura de arquivos. \
carregar_arquivo_html  :: Como carregar um arquivo html utilizando o render e namespace. \
passar_variavel_html  ::  Passando uma variável do python para dentro do html. \
dinamic_links  ::  Criando links dinâmicos dentro da Tag <a href= > \  
dinamic_html_content  ::  Criando conteúdo html de forma dinâmica. \
arquivo_parcial_html  ::  Entendendo como reutilizar fragmentos de código html. \
variavel_partial_template  ::  Passando uma variável para dentro do partial snipet code. \
arquivos_estaticos  ::  Arquivos estáticos são arquivos não modificáveis organizados no projeto. \
load_static_images  ::  Carregando imagens. \
load_css  ::  Carregando arquivo css do App e de forma global. \
argumento_pela_url  ::  Uma view recebe um argumento passado pela url do navegador. \
urls_dinamicas  ::  Indicar o path de uma URL com a função reverse sem indicar todo o caminho de forma manual. \
url_dtl_tag  ::  Como passar uma URL dinâmica usando a tag URL do Django Template Language (DTL) .\
aplicando_filtros  ::  Aplicando filtros no html dinâmico. \
template_blocks  ::  Como aproveitar uma estrutura já criada em html que servirá como base. \
heranca_de_template_html  ::  Herança de tempĺates html. \
partials  ::  Criando snipets codes em html. \
error_404  ::  Retornando uma página de erro 404. \
loop_com_for  ::  Executando um loop for dentro de uma estrutura html. \
list_with_for_tag  :: Iterando listas com a tag for do Django. \
if_statement  ::  Utilizando o if com código html. \
models  ::  Entendendo sobre os modelos do Django. \
formulario  ::  Criando um formulario para registro utilizando os models. \
formulario_manual  ::  Inserindo campos do formulário manualmente no html. \
book_store  ::  Entendendo um pouco mais sorbe modelos do django. \
monthly_challenges  ::  Aplicação com as estruturas básicas de html e url dinâmicas, principais tags, herança de template e arquivos estáticos. \
partial_blog_project  ::  Primeira parte do projeto do site blog: templates, arquivos estáticos, partials snipets, dummy data, lógica dos views. \
blog  ::  Criando um blog. \


OBS: Ler o arquivo 'objetivos.txt' de cada projeto para um resumo dos
tópicos de cada exemplo.

## ROTEIRO CRIAÇÃO DE UM PROJETO
1 - Criar a pasta do projeto e a máquina virtual.\
2 - django-admin startproject <nome_projeto> . (Cria o projeto na pasta atual ".")\
3 - python manage.py startapp <nome_do_app> (Para criar um App)\
4 - Editar seetings.py em installed_apps. \
5 - Criar a pasta templates/app_<nome> dentro do app principal.\
6 - Criar o home.html \
7 - Criar arquivo app/urls.py \
8 - Editar arquivo app/views.py \
9 - Checar com startrunserver

## ESTRUTURAS DE ARQUIVO DO PROJETO DJANGO
```
\Pasta Inicial do Projeto
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
        settings.py - Possui diversas configurações globais do projeto no django.
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
                \partials - Pasta com códigos parciais html.
                \pages - Pasta de arquivos html do App
                    home.thml - Exemplo de uma página html do pertencente ao App.
        \static - Pasta com os arquivos estáticos do App.
            \App - Pasta namespace.
                \css - Pasta de arquivos CSS do App.
                    style.css - Arquivo de código css do App
    \base_templates - Pasta com os tipos de arquivos templates globais
        \global - Pasta namespace global
    \base_static
        \global - Pasta com os tipos de arquivos estáticos globais.
    \venv - Pasta da máquina virtual do python.
        \bin
            activate - Script de ativação da máquina virtual do python.
```

## LINKS ÚTEIS
Códigos de status de respostas HTTP: [MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status).\
Métodos de requisição HTTP: [MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods).\
Tipos de campos do model: [Documentação Oficial](https://docs.djangoproject.com/pt-br/3.2/ref/models/fields/).\
Validação de dados no model: [Documentação Oficial](https://docs.djangoproject.com/en/5.0/ref/validators/). \
Django Template Language - Filtros: [Documentação Oficial](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/). \
QuerySet API reference: [Documentação Oficial](https://docs.djangoproject.com/pt-br/3.2/ref/models/querysets/). \
On-Line SQLite Viewer: [Site](https://sqliteviewer.app/). \
Making Queries with Field lookups: [Documentação Oficial](https://docs.djangoproject.com/en/5.0/topics/db/queries/). \
Delete multiple model instances [Documentação Oficial](https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects). \
Update multiple model instances [Documentação Oficial](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update). \
Create multiple model instances [Documentação Oficial](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create).


## COMANDOS DJANGO IMPORTANTES
$python3 manage.py collectstatic - Coleta os arquivos estáticos agrupando na pasta
indicada no STATIC_ROOT do settings.py \
$python3 manage.py runserver - Roda o servidor de desenvolvimento no endereço http://127.0.0.1:8000/ \
$python3 manage.py makemigrations - Cria os arquivos de migração dentro da pasta migrations. \
$python3 manage.py migrate - Executa as migrações para a base de bados. \
$python3 manage.py createsuperuser - Cria o usuário root para a seção do administrador
(127.0.0.1:8000/admin) \
$python3 manage.py shell - Abre o shell do Django
