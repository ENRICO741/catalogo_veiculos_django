from django.contrib import admin

from app_catalogo_veiculos import models
# Register your models here.
@admin.register(models.Carro)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id_carro', 'nome', 'marca', 'ano', 'image', 'preco'
    ordering = 'id_carro',
    search_fields = 'id_carro', 'nome', 'marca', 'ano',
