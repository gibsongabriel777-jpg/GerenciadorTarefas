from datetime import date, timedelta

from models.usuario import Usuario
from models.categoria import Categoria
from models.tarefa_comum import TarefaComum
from models.tarefa_recorrente import TarefaRecorrente
from services.relatorio_tarefas import RelatorioTarefas


def demonstrar_sistema():
    # Criando o usuario e seu quadro de tarefas
    usuario = Usuario("Gibson", "Gibson@email.com")
    quadro = usuario.criar_quadro("Faculdade")

    # Criando categorias
    faculdade = Categoria("Faculdade", "azul")
    pessoal = Categoria("Pessoal", "verde")

    # Criando tarefas de tipos diferentes
    tarefa1 = TarefaComum(
        "Estudar Python",
        "Revisar classes e objetos",
        date.today() + timedelta(days=2),
        "Alta",
        faculdade
    )

    tarefa2 = TarefaRecorrente(
        "Fazer exercícios",
        "Praticar programação",
        date.today(),
        "Média",
        pessoal,
        intervalo_dias=7
    )

    
    quadro.adicionar_tarefa(tarefa1)
    quadro.adicionar_tarefa(tarefa2)

    
    tarefa1.concluir()

    #polimorfismo
    print("TIPOS DE TAREFA")
    for tarefa in quadro.listar_tarefas():
        print(f"- {tarefa.titulo}: {tarefa.obter_tipo()}")

    # Consultando tarefas
    print("\nTAREFAS CADASTRADAS")
    for tarefa in quadro.listar_tarefas():
        status = "Concluída" if tarefa.concluida else "Pendente"
        print(f"- {tarefa.titulo} | Prazo: {tarefa.prazo} | "
              f"Prioridade: {tarefa.prioridade} | Status: {status}")

    # Gerando relatório dependência, pois recebe o quadro)
    relatorio = RelatorioTarefas()
    print("\nRELATÓRIO")
    print(relatorio.gerar_resumo(quadro))

    # Demonstrando geração da próxima tarefa recorrente
    proxima = tarefa2.gerar_proxima()
    print("\nPRÓXIMA OCORRÊNCIA")
    print(f"{proxima.titulo} - {proxima.prazo}")


if __name__ == "__main__":
    demonstrar_sistema()
