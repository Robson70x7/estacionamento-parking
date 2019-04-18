from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField ()
    telefone = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)