from django.contrib import admin
<<<<<<< HEAD
from .models import Projeto, Tarefa

admin.site.register(Tarefa)
=======
from .models import Projeto 

# Register your models here.

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio')
    search_fields = ('nome',)
>>>>>>> main
