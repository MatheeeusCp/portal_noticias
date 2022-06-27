from datetime import datetime
from django.db import models


class Genero(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Noticia(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    url_imagem = models.TextField()
    nome_autor = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
