from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastrar(request):
    return render(request, 'turma/cadastroTurma.html')

def listar(request):
    return render(request, 'turma/listarTurmas.html')

def ausencia(request):
    return render(request, 'turma/registroAusencia.html')