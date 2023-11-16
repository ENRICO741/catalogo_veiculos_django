from rest_framework import serializers
from app_catalogo_veiculos import models
class CatalogoVeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carro
        fields = '__all__'
        