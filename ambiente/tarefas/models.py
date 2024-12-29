from django.db import models

from .choices import TarefaChoice

class Tarefa(models.Model):
    nome_tarefa = models.CharField(max_length=255)
    descricao_tarefa = models.TextField(blank=True, null=True)
    status_tarefa = models.CharField(
        "Status da tarefa",
        choices=TarefaChoice.CHOICES,
        default=TarefaChoice.PENDENTE,
        max_length=12,
    )
