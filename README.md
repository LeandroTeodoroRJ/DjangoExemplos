# PROJETO DJANGO.
## INSTALAÇÃO E CONFIGURAÇÃO DE AMBIENTE
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install git curl build-essential dkms perl wget -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
  libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```


## ORDEM SUGERIDA DE LEITURA DOS PROJETOS.
hello_django  ::  Primeiro exemplo no framework Django.\
boillerplate  ::  Escrevendo uma estrutura básica de projetos Django.\
utilizando_apps \
carregar_arquivo_html  \
passar_variavel_html  \
arquivo_parcial_html  \
arquivos_estaticos  \

OBS: Ler o arquivo 'objetivos.txt' de cada projeto para um resumo dos
tópicos de cada exemplo.

## ROTEIRO CRIAÇÃO DE PROJETO
1 - Criar a pasta do projeto e a máquina virtual.\
2 - django-admin startproject.\
3 - python manage.py startapp.\
4 - Editar seetings.py em installed_apps.\
5 - Criar a pasta templates/app_<nome> dentro do app principal.\
6 - Criar o home.html \
7 - Criar arquivo app/urls.py \
8 - Editar arquivo app/views.py \
9 - Checar com startrunserver \

## ESTRUTURAS DE ARQUIVO DO PROJETO DJANGO
```
<Pasta Raíz do Projeto>
> <.mypy_cache> - Arquivos de cache do plug-in MyPy do VS code
> <Projeto> - Pasta do projeto iniciado com startproject do django
>> <__pychache__> - Pasta de cache do python
> __init.py__  - Pode ser utilizado como arquivo de inicialização do pacote.
> asgi.py - Utilizado para fazer a ligação com o servidor Web
> wsgi.py - Utilizado para fazer a ligação com o servidor Web
> urls.py - Faz a ligação com o DNS no navegador
> settings.py - Arquivo de configuração do django
> <venv> - Pasta da máquina virtual do python
>> <bin>
>> activate - Script de ativação da máquina virtual do python
.gitignore - Arquivo de pastas que devem ser ignoradas ao subir o código para o github.
db.sqlite3 - Arquivo de banco de dados do sqlite3
manage.py - Arquivo que tem a mesma função do comando djando-admin, antes da execução do manage.py ele carrega as configurações do arquivo settings.py
> <App> - Pasta do App
> viwes.py - Arquivo de renderização das páginas (views)
> urls.py - Arquivo que importas as funções das viwes e interliga ao dominio url do App
>> <static> - Pasta com os arquivos estáticos do App (utilizar namespace)
>> <template> - Pasta com templates html (utilizar namespace)
>>> <partials> - Pasta com códigos parciais html
>>> <pages> - Pasta com as páginas html
> <base_static/global> - Pasta com os tipos de arquivos estáticos globais
> <base_templates/global> - Pasta com os tipos de arquivos templates globais
```
