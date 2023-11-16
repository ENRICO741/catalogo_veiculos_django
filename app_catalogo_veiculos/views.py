from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carro

# Create your views here.


def carros(request):

    carros = {
        'carros': Carro.objects.all().order_by('preco')
    }

    return render(request,'carros/carros.html', carros)

@login_required
def create_carro(request):

    carros = {
        'carros': Carro.objects.all().order_by('preco')
    }

    return render(request,'carros/listagem_carros.html', carros)

def salvar(request):

    novo_carro = Carro()
    novo_carro.nome = request.POST.get('nome')
    novo_carro.marca = request.POST.get('marca')
    novo_carro.ano = request.POST.get('ano')
    novo_carro.image = request.POST.get('image')
    novo_carro.preco = request.POST.get('preco')
    novo_carro.save()

    carros = {
        'carros': Carro.objects.all().order_by('preco')
    }

    return render(request,'carros/listagem_carros.html', carros)

def editar(request, id):
    carro = Carro.objects.get(id_carro=id)

    return render(request, 'carros/update.html', {"carro": carro})

def update(request, id):
    new_nome = request.POST.get('nome')
    new_marca = request.POST.get('marca')
    new_ano = request.POST.get('ano')
    new_image = request.POST.get('image')
    new_preco = request.POST.get('preco')
    carro = Carro.objects.get(id_carro=id)
    carro.nome = new_nome
    carro.marca = new_marca
    carro.ano = new_ano
    carro.image = new_image
    carro.preco = new_preco
    carro.save()

    return redirect(create_carro)

def delete(request, id):
    carro = Carro.objects.get(id_carro=id)
    carro.delete()

    return redirect(create_carro)