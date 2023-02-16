from django.shortcuts import redirect, render
from .forms import ContactForm, ProdutoModelForm
from django.contrib import messages

from .models import Produto

def index(request):
  context = {
    'produtos': Produto.objects.all()
  }
  return render(request, 'index.html', context)

def contact(request):
  # Formulário usado quando não precisamos salvar os dados no banco de dados
  form = ContactForm(request.POST or None)

  if (str(request.method )== 'POST'):
    if (form.is_valid()):
      form.send_mail()
      messages.success(request, 'Email enviado com sucesso.')
      form = ContactForm() # Limpando o formulário
    else: 
      messages.error(request, 'Erro ao enviar o email.')

  context = {
    'form': form
  }

  return render(request, 'contact.html', context)

def product(request):
  if (str(request.user) != 'AnonymousUser'):
    if (str(request.method) == "POST"):
      form = ProdutoModelForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        messages.success(request, "Produto salvo com sucesso.")
        form = ProdutoModelForm()
      else:
        messages.error(request, "Erro ao salvar o produto.")
    else:
      form = ProdutoModelForm()
    context = {
      'form': form
    }
    return render(request, 'product.html', context)
  else:
    return redirect("index")
