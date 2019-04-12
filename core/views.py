from django.shortcuts import render, redirect
from . import models, forms


def home(request):
    template_name = 'base.html'
    context = {'mensagem': 'ola mundo'}
    return render(request, template_name, context)


def lista_pessoas(request):
    pessoas = models.Pessoa.objects.all()
    form = forms.PessoaForm()
    context = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/listar_pessoas.html', context)


def pessoa_novo(request):
    form = forms.PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    return redirect('core:lista_pessoas')


def lista_veiculos(request):
    veiculos = models.Veiculo.objects.all()
    form = forms.VeiculoForm()
    context = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/listar_veiculos.html', context)


def veiculo_novo(request):
    form = forms.VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_veiculos')


def lista_movrotativos(request):
    mov_rots = models.MovRotativo.objects.all()
    form = forms.MovRotativoForm()
    context_data = {'mov_rots':mov_rots, 'form':form}
    return render(request, 'core/listar_mov_rot.html', context_data)


def movrotativo_novo(request):
    form = forms.MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_movrotativos')


def lista_mensalistas(request):
    mesalistas = models.Mensalista.objects.all()
    form = forms.MensalistaForm()
    context_data = {'mensalistas':mesalistas, 'form': form}
    return render(request, 'core/lista-mensalistas.html', context_data)


def mensalista_novo(request):
    form = forms.MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_mensalistas')


def lista_movmensalistas(request):
    mov_menslistas = models.MovMensalista.objects.all()
    form = forms.MovMensalistaForm()
    context_data = {'mov_mensalistas':mov_menslistas, 'form': form}
    return render(request, 'core/lista-movmensalistas.html', context_data)


def movmesalista_novo(request):
    form = forms.MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_mensalistas')
