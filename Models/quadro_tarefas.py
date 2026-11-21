class QuadroTarefas:
    def __init__(self, nome):
        if not nome:
            raise ValueError("O quadro precisa ter um nome.")

        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            return False

        self.tarefas.append(tarefa)
        return True

    def remover_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                return True
        return False

    def listar_tarefas(self):
        return self.tarefas.copy()

    def buscar_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None
