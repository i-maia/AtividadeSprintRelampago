from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(
        max_length=20,
        choices=[('Baixa', 'Baixa'), ('Média', 'Média'), ('Alta', 'Alta')],
        default='Média'
    )
    concluido = models.BooleanField(default=False)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return f"{self.titulo} - {self.projeto.nome}"