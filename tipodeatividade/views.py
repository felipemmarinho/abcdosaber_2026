from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastrar(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')

def listar(request):
    return render(request, 'tipodeatividade/listarTiposAtividade.html')
