from django import forms
from . import models


class PessoaForm(forms.ModelForm):
    class Meta:
        model = models.Pessoa
        fields = ('__all__')


class VeiculoForm(forms.ModelForm):
    class Meta:
        fields = ('__all__')
        model = models.Veiculo


class MovRotativoForm(forms.ModelForm):
    class Meta:
        fields = ('__all__')
        model = models.MovRotativo