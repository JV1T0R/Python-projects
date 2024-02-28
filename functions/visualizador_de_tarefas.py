def visualizar_todas_tarefas(tarefas):
    for titulo, tarefa in tarefas.items():
        print(f"\nTítulo: {titulo}\nDescrição: {tarefa['Descrição']}\nPrioridade: {tarefa['Prioridade']}\nCategoria: {tarefa['Categoria']}")


def filtrar_tarefas_prioridade(tarefas):
    selecionar_prioridade = str(input("Digite a Categoria para Filtrar as Tarefas: "))
    for titulo, tarefa in tarefas.items():
        if selecionar_prioridade == tarefa['Prioridade']:
            print(f"\nTítulo: {titulo}\nDescrição: {tarefa['Descrição']}\nPrioridade: {tarefa['Prioridade']}\nCategoria: {tarefa['Categoria']}")
        else:
            print("Prioridade Invalída")


def filtrar_tarefas_categaoria(tarefas):
    selecionar_categoria = str(input("Digite a Categoria para Filtrar as Tarefas: "))
    for titulo, tarefa in tarefas.items():
        if selecionar_categoria == tarefa['Categoria']:
            print(f"\nTítulo: {titulo}\nDescrição: {tarefa['Descrição']}\nPrioridade: {tarefa['Prioridade']}\nCategoria: {tarefa['Categoria']}")
        else:
            print("Categoria Invalída")


