from django.shortcuts import render, redirect
from . import forms

def home(request):
    template_name = 'website/index.html'
    return render(request, template_name)

def contato(request):
    template_name = 'website/contato.html'
    form = forms.ContatoForm(request.POST or None)
    data = {'form':form}
    if 'mensagem' in request.session:
        data['mensagem'] = request.session.pop('mensagem')
    return render(request, template_name, data)


def servico(request):
    template_name = 'website/servico.html'
    return render(request, template_name)


def save_contato(request):
    form = forms.ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        request.session['mensagem'] = "Enviado com sucesso"
    else:
        request.session['mensagem'] = "Formulario inválido"
        return render(request, 'webstite/contato.html', {'form':form})

    return redirect('website:contato')
