from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/excluir/', views.excluir_projeto, name='excluir_projeto'),
]