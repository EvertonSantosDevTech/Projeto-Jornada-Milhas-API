from django.db import models


class Depoimento(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_de_registro = models.DateField()
    depoimento_descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return self.nomeCompleto


class Destino(models.Model):

    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    foto1 = models.ImageField(null=True, blank=True)
    foto2 = models.ImageField(null=True, blank=True)
    meta = models.CharField(max_length=160, default="")
    texto_descritivo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome
