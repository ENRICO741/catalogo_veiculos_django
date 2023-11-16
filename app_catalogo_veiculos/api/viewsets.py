from rest_framework import viewsets
from app_catalogo_veiculos.api import serializers
from app_catalogo_veiculos import models

class CatalogoVeiculosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CatalogoVeiculosSerializer
    queryset = models.Carro.objects.all()