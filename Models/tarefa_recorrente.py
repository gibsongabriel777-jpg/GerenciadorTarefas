from datetime import timedelta
from models.tarefa import Tarefa


class TarefaRecorrente(Tarefa):
    def __init__(self, titulo, descricao, prazo, prioridade, categoria,
                 intervalo_dias):
        if not isinstance(intervalo_dias, int) or intervalo_dias <= 0:
            raise ValueError("O intervalo deve ser um número inteiro positivo.")

        super().__init__(titulo, descricao, prazo, prioridade, categoria)
        self.intervalo_dias = intervalo_dias

    def obter_tipo(self):
        return "Tarefa recorrente"

    def gerar_proxima(self):
        novo_prazo = self.prazo + timedelta(days=self.intervalo_dias)

        return TarefaRecorrente(
            self.titulo,
            self.descricao,
            novo_prazo,
            self.prioridade,
            self.categoria,
            self.intervalo_dias
        )
