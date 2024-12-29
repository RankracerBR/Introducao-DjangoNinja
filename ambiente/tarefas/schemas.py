from ninja import Schema
from typing import Optional


class TarefaSchema(Schema):
    nome_tarefa: str
    descricao_tarefa: Optional[str] = None
    status_tarefa: str

    class Config:
        orm_mode = True


class DeletarTarefaSchema(Schema):
    nome_tarefa: str
