from django.db import models

# Create your models here.

class Carro(models.Model):
    id_carro = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    marca = models.TextField(max_length=255)
    ano = models.IntegerField()
    image = models.ImageField()
    preco = models.FloatField()
