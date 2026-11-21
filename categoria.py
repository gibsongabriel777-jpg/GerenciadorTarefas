class Categoria:
    def __init__(self, nome, cor="cinza"):
        if not nome:
            raise ValueError("O nome da categoria não pode ficar vazio.")

        self.nome = nome
        self.cor = cor

    def __str__(self):
        return self.nome
