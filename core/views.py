from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
import io

@login_required
def home(request):
    template_name = 'core/index.html'
    return render(request, template_name)

@login_required
def lista_pessoas(request):
    pessoas = models.Pessoa.objects.all()
    form = forms.PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/listar_pessoas.html', data)

@login_required
def pessoa_novo(request):
    form = forms.PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    return redirect('core:lista_pessoas')

@login_required
def pessoa_update(request, pk):
    pessoa = models.Pessoa.objects.get(pk=pk)
    form = forms.PessoaForm(request.POST or None, instance=pessoa)
    data =  {'form':form, 'pessoa':pessoa}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:lista_pessoas')

    return render(request, 'core/pessoa_update.html', data)

@login_required
def pessoa_delete(request, pk):
    pessoa_delete = models.Pessoa.objects.get(pk=pk)
    data = {'obj':pessoa_delete}

    if request.method == 'POST':
        pessoa_delete.delete()
        return redirect('core:lista_pessoas')

    return render(request, 'core/confirm_delete.html', data)

@login_required
def lista_veiculos(request):
    veiculos = models.Veiculo.objects.all()
    form = forms.VeiculoForm()
    context = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/listar_veiculos.html', context)

@login_required
def veiculo_novo(request):
    form = forms.VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_veiculos')

@login_required
def veiculo_update(request, pk):
    veiculo = models.Veiculo.objects.get(id=pk)
    form = forms.VeiculoForm(request.POST or None, instance=veiculo)
    data = { 'form': form, 'veiculo':veiculo }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:lista_veiculos')

    return render(request, 'core/veiculo_update.html', data)

@login_required
def veiculo_delete(request, pk):
    veiculo = models.Veiculo.objects.get(pk=pk)
    data = {'obj':veiculo}

    if request.method == 'POST':
        veiculo.delete()
        return redirect('core:lista_veiculos')

    return render(request, 'core/confirm_delete.html',data)

@login_required
def lista_movrotativos(request):
    mov_rots = models.MovRotativo.objects.all()
    form = forms.MovRotativoForm()
    context_data = {'mov_rots':mov_rots, 'form':form}
    return render(request, 'core/listar_mov_rot.html', context_data)

@login_required
def movrotativo_novo(request):
    form = forms.MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_movrotativos')

@login_required
def movrotativo_update(request, pk):
    mov_rotativo = models.MovRotativo.objects.get(pk=pk)
    form = forms.MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data = {'form':form, 'mov_rotativo':mov_rotativo}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:lista_movrotativos')

    return render(request, 'core/movrotativo_update.html',data)

@login_required
def movrotativo_delete(request, pk):
    movrotativo = models.MovRotativo.objects.get(pk=pk)
    data = {'obj':movrotativo}

    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core:lista_movrotativos')

    return render(request, 'core/confirm_delete.html', data)

@login_required
def lista_mensalistas(request):
    mesalistas = models.Mensalista.objects.all()
    form = forms.MensalistaForm()
    context_data = {'mensalistas':mesalistas, 'form': form}
    return render(request, 'core/lista-mensalistas.html', context_data)

@login_required
def mensalista_novo(request):
    form = forms.MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_mensalistas')

@login_required
def mensalista_update(request, pk):
    mensalista = models.Mensalista.objects.get(pk=pk)
    form = forms.MensalistaForm(request.POST or None, instance=mensalista)
    data = {'form':form, 'mensalista':mensalista}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:lista_mensalistas')

    return render(request, 'core/mensalista_update.html',data)

@login_required
def mensalista_delete(request, pk):
    mensalista = models.Mensalista.objects.get(pk=pk)
    data = {'obj':mensalista}

    if request.method == 'POST':
        mensalista.delete()
        return redirect('core:lista_mensalistas')

    return render(request, 'core/confirm_delete.html', data)

@login_required
def lista_movmensalistas(request):
    mov_menslistas = models.MovMensalista.objects.all()
    form = forms.MovMensalistaForm()
    context_data = {'mov_mensalistas':mov_menslistas, 'form': form}
    return render(request, 'core/lista-movmensalistas.html', context_data)

@login_required
def movmesalista_novo(request):
    form = forms.MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:lista_mensalistas')

@login_required
def movmensalista_update(request, pk):
    movmensalista = models.MovMensalista.objects.get(pk=pk)
    form = forms.MovMensalistaForm(request.POST or None, instance=movmensalista)
    data = {'form':form, 'movmensalista':movmensalista}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:lista_movmensalistas')

    return render(request, 'core/movmensalista_update.html', data)

@login_required
def movmensalista_delete(request, pk):
    movmensalista = models.MovMensalista.objects.get(pk=pk)
    data = {'obj':movmensalista}

    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core:lista_movmensalistas')

    return render(request, 'core/confirm_delete.html', data)

class Render:
    @staticmethod
    def render(template_name: str, params: dict, filename: str):
        template = get_template(template_name)
        html = template.render(params)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment;filename={filename}.pdf'
        pdf = pisa.CreatePDF(html, dest=response)
        if not pdf.err:
            return response
        else:
            return HttpResponse('Error Rendering pdf', status=400)


class CreatePdf(View):
    def get(self, request):
        veiculos = models.Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }

        return Render.render('core/relatorio_pdf.html', params, 'relatorio_veiculos')
