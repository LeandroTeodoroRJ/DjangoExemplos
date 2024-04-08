from django.db import models

# Create your models here.
# É possível criar um model a partir de uma classe.

class Condutor(models.Model):
    nome = models.CharField(max_length=40)
    def __str__(self):
        return self.nome    #Retorna o nome na página de administração


class Carro(models.Model):
    placa = models.CharField(max_length=10) #Equivalente ao Varchar
    modelo = models.CharField(max_length=10)
    Marca = models.CharField(max_length=10)
    ano = models.IntegerField()  #Atribuno numérico
    novo = models.BooleanField(default=False)  #Campo booleano
    sinistros = models.TextField()  #Campo texto sem limite máximo
    slug = models.SlugField()
    #Relacionamento para a tabela Condutor
    condutor = models.ForeignKey(Condutor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.placa    #Retorna o nome na página de administração
