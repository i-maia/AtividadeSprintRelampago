from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
]