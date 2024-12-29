from ninja import NinjaAPI

from django.shortcuts import get_object_or_404

from .models import Tarefa
from .schemas import TarefaSchema, DeletarTarefaSchema

api_tarefa = NinjaAPI(urls_namespace="tarefas")


class TarefaAPI:
    @staticmethod
    @api_tarefa.get("/tarefas/listar_tarefas")
    def listar_tarefas(request):
        return [TarefaSchema.model_validate(tarefa)
                 for tarefa in Tarefa.objects.all()]
    
    @staticmethod
    @api_tarefa.post("/tarefas/criar_tarefa", response={200: TarefaSchema,
                                                        400: dict})
    def criar_tarefa(request, tarefa: TarefaSchema):
        try:
            tarefa_data = tarefa.model_dump()

            # Create the task
            instancia_tarefa = Tarefa.objects.create(
                nome_tarefa=tarefa_data["nome_tarefa"],
                descricao_tarefa=tarefa_data.get("descricao_tarefa", ""),
                status_tarefa=tarefa_data["status_tarefa"],
            )

            return TarefaSchema.model_validate(instancia_tarefa)

        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    @api_tarefa.delete("/tarefas/remover_tarefa", 
                    response={200: DeletarTarefaSchema, 400: dict})
    def deletar_tarefa(request, payload: DeletarTarefaSchema):
        nome_tarefa = payload.nome_tarefa

        # Fetch the task or raise 404 if not found
        tarefa = get_object_or_404(Tarefa, nome_tarefa=nome_tarefa)

        try:
            # Delete the task
            tarefa.delete()

            # Return the deleted task's name as response
            return {"nome_tarefa": nome_tarefa}

        except Exception as e:
            return {
                400: {
                    "error": f"Erro ao deletar a tarefa '{nome_tarefa}': {str(e)}"
                }
            }
