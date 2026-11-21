class RelatorioTarefas:
    def calcular_total(self, quadro):
        return len(quadro.listar_tarefas())

    def calcular_concluidas(self, quadro):
        return sum(1 for tarefa in quadro.listar_tarefas()
                   if tarefa.concluida)

    def calcular_pendentes(self, quadro):
        return sum(1 for tarefa in quadro.listar_tarefas()
                   if not tarefa.concluida)

    def calcular_atrasadas(self, quadro):
        return sum(1 for tarefa in quadro.listar_tarefas()
                   if tarefa.esta_atrasada())

    def gerar_resumo(self, quadro):
        return (
            f"Quadro: {quadro.nome}\n"
            f"Total de tarefas: {self.calcular_total(quadro)}\n"
            f"Concluídas: {self.calcular_concluidas(quadro)}\n"
            f"Pendentes: {self.calcular_pendentes(quadro)}\n"
            f"Atrasadas: {self.calcular_atrasadas(quadro)}"
        )
