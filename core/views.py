from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm

# Create your views here.

def listar_projetos(request):
    projetos = Projeto.objects.all().order_by('-data_inicio')

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')

    else:
        form = ProjetoForm()

    contexto = {
        'projetos': projetos,
        'form': form
    }

    return render(request, 'core/projetos.html', contexto)


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Projeto "{projeto.nome}" atualizado com sucesso!')
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    contexto = {
        'form': form,
        'projeto': projeto
    }

    return render(request, 'core/editar_projeto.html', contexto)


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        nome = projeto.nome
        projeto.delete()
        messages.success(request, f'Projeto "{nome}" excluído com sucesso!')

    contexto = {
        'projeto': projeto
    }

    return render(request, 'core/excluir_projeto.html', contexto)

