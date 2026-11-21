from models.tarefa import Tarefa


class TarefaComum(Tarefa):
    def obter_tipo(self):
        return "Tarefa comum"
