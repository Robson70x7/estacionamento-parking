from django.shortcuts import render
from .models import Pessoa,  Veiculo, MovRotativo

def home(request):
    template_name = 'base.html'
    return render(request, template_name, {'mensagem': 'ola mundo'})

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/listar_pessoas.html', {'pessoas':pessoas})

def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/listar_veiculos.html', {'veiculos':veiculos})

def listar_movrotativos(request):
    mov_rots = MovRotativo.objects.all()
    return render(request, 'core/listar_mov_rot.html', {'mov_rots':mov_rots})