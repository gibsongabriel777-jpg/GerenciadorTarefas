from abc import ABC, abstractmethod
from datetime import date
from uuid import uuid4


class Tarefa(ABC):
    def __init__(self, titulo, descricao, prazo, prioridade, categoria):
        if not titulo:
            raise ValueError("O título da tarefa não pode ficar vazio.")

        if not isinstance(prazo, date):
            raise TypeError("O prazo deve ser uma data.")

        prioridades_validas = ["Baixa", "Média", "Alta"]
        if prioridade not in prioridades_validas:
            raise ValueError("Prioridade deve ser Baixa, Média ou Alta.")

        self.id = str(uuid4())
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = False
        self.categoria = categoria #guarda o objeto categoria criado

    def concluir(self):
        self.concluida = True

    def reabrir(self):
        self.concluida = False

    def esta_atrasada(self):
        return not self.concluida and self.prazo < date.today()

    @abstractmethod
    def obter_tipo(self):
        pass
