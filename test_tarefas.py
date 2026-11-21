import unittest
from datetime import date, timedelta

from models.usuario import Usuario
from models.categoria import Categoria
from models.tarefa_comum import TarefaComum
from models.tarefa_recorrente import TarefaRecorrente
from services.relatorio_tarefas import RelatorioTarefas


class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("Carlos", "carlos@email.com")
        self.quadro = self.usuario.criar_quadro("Estudos")
        self.categoria = Categoria("Faculdade")

        self.tarefa = TarefaComum(
            "Estudar UML",
            "Revisar diagrama de classes",
            date.today() + timedelta(days=3),
            "Alta",
            self.categoria
        )

    def test_criar_usuario_e_quadro(self):
        self.assertEqual(self.usuario.get_nome(), "Carlos")
        self.assertEqual(len(self.usuario.listar_quadros()), 1)

    def test_adicionar_e_listar_tarefa(self):
        self.assertTrue(self.quadro.adicionar_tarefa(self.tarefa))
        self.assertEqual(len(self.quadro.listar_tarefas()), 1)

    def test_nao_adicionar_mesma_tarefa_duas_vezes(self):
        self.quadro.adicionar_tarefa(self.tarefa)
        self.assertFalse(self.quadro.adicionar_tarefa(self.tarefa))

    def test_buscar_tarefa(self):
        self.quadro.adicionar_tarefa(self.tarefa)
        encontrada = self.quadro.buscar_tarefa(self.tarefa.id)
        self.assertEqual(encontrada, self.tarefa)

    def test_remover_tarefa(self):
        self.quadro.adicionar_tarefa(self.tarefa)
        self.assertTrue(self.quadro.remover_tarefa(self.tarefa.id))
        self.assertEqual(len(self.quadro.listar_tarefas()), 0)

    def test_concluir_e_reabrir(self):
        self.tarefa.concluir()
        self.assertTrue(self.tarefa.concluida)

        self.tarefa.reabrir()
        self.assertFalse(self.tarefa.concluida)

    def test_tipos_diferentes(self):
        recorrente = TarefaRecorrente(
            "Exercícios", "Praticar", date.today(),
            "Média", self.categoria, 7
        )
        self.assertEqual(self.tarefa.obter_tipo(), "Tarefa comum")
        self.assertEqual(recorrente.obter_tipo(), "Tarefa recorrente")

    def test_gerar_proxima_recorrencia(self):
        recorrente = TarefaRecorrente(
            "Exercícios", "Praticar", date.today(),
            "Média", self.categoria, 7
        )
        proxima = recorrente.gerar_proxima()
        self.assertEqual(proxima.prazo, date.today() + timedelta(days=7))
        self.assertIsInstance(proxima, TarefaRecorrente)

    def test_relatorio(self):
        self.quadro.adicionar_tarefa(self.tarefa)
        self.tarefa.concluir()

        relatorio = RelatorioTarefas()
        self.assertEqual(relatorio.calcular_total(self.quadro), 1)
        self.assertEqual(relatorio.calcular_concluidas(self.quadro), 1)
        self.assertEqual(relatorio.calcular_pendentes(self.quadro), 0)

    def test_validar_prioridade(self):
        with self.assertRaises(ValueError):
            TarefaComum(
                "Tarefa inválida", "Descrição", date.today(),
                "Urgente", self.categoria
            )


if __name__ == "__main__":
    unittest.main()
