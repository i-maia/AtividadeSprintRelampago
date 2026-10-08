from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
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

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/lista_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'core/form_tarefa.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/form_tarefa.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'core/confirma_exclusao_tarefa.html', {'tarefa': tarefa})