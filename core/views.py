from django.shortcuts import render, redirect
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