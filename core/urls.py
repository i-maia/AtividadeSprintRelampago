from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/editar/<int:pk>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
]