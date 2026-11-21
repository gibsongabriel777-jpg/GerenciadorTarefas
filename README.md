# Gerenciador de Tarefas
Projeto acadêmico em Python com foco em Programação Orientada a Objetos.

## Executar a demonstração
Na pasta raiz do projeto:
python main.py

## Executar os testes
Na pasta raiz do projeto:
python -m unittest discover -s tests -v

## Relações entre as classes
- Herança: `TarefaComum` e `TarefaRecorrente` herdam de `Tarefa`.
- Polimorfismo: as subclasses implementam `obter_tipo()` de formas diferentes.
- Composição: `QuadroTarefas` contém e gerencia uma coleção de tarefas.
- Associação: `Usuario` mantém quadros; cada `Tarefa` mantém uma referência à sua `Categoria`.
- Dependência: `RelatorioTarefas` recebe um `QuadroTarefas` para calcular estatísticas.

## Observação sobre composição
 O quadro controla a inclusão e remoção das tarefas. A regra de exclusão do quadro e de suas tarefas deve ser mantida pela camada que controla o quadro.
