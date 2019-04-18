from django.shortcuts import render
from . import forms

def home(request):
    template_name = 'website/index.html'
    return render(request, template_name)

def contato(request):
    template_name = 'website/contato.html'
    form = forms.ContatoForm(request.POST or None)
    data = {'form':form}
    return render(request, template_name, data)

def servico(request):
    template_name = 'website/servico.html'
    return render(request, template_name)