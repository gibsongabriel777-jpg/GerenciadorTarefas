from models.quadro_tarefas import QuadroTarefas


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.quadros = []

    def criar_quadro(self, nome):
        quadro = QuadroTarefas(nome)
        self.quadros.append(quadro)
        return quadro

    def listar_quadros(self):
        return self.quadros.copy()

    def get_nome(self):
        return self.nome
