from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def mostrar_hello(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.save()

    return render(request, 'index.html')

def monstrar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'pessoas.html', {'dados': pessoas})