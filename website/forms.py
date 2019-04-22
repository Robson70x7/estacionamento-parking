from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .mail import send_mail_template

class ContatoForm(forms.Form):
    nome = forms.CharField ()
    telefone = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField(max_length=60)
    mensagem = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        subject = self.cleaned_data['assunto']
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            'mensagem': self.cleaned_data['mensagem'],
        }
        message = f"Nome: {context['nome']}; e-mail: {context['email']}; Telefone: {context['telefone']}; mensagem: {context['mensagem']}  "
        from_email = settings.DEFAULT_FROM_EMAIL
        recepient_list = [settings.CONTACT_EMAIL]
        template_name = 'website/mail_template.html'

        # Send the mail
        send_mail_template(subject, template_name, context, recepient_list)
        
        