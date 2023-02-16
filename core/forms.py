from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContactForm(forms.Form):
  name = forms.CharField(label='Nome', max_length=35, min_length=3)
  email = forms.EmailField(label="Email", max_length=35)
  subject = forms.CharField(label="Assunto", max_length=50)
  message = forms.CharField(label="Mensagem", widget=forms.Textarea())

  def send_mail(self):
    nome = self.cleaned_data['name']
    email = self.cleaned_data['email']
    subject = self.cleaned_data['subject']
    message = self.cleaned_data['message']

    content = f'Nome: {nome}\nEmail: {email}\nAssunto: {subject}\nMensagem: {message}'
   
    mail = EmailMessage(
      subject="Email enviado pelo django.",
      body=content,
      from_email='contato@seudominio.com.br',
      to=['contato@seudominio.com.br'], # Podemos enviar para todos os emails dessa lista
      headers={"Reply-To": email}
    )
    mail.send()

class ProdutoModelForm(forms.ModelForm): # ModelForm tem comportamentos diferentes
  class Meta: # Passo metadados 
    model = Produto
    fields = ['name', 'price', 'thumbnail']