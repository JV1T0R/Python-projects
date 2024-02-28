def concluir_tarefa(tarefas):
    selecionar_tarefa = input("Digite o Título da Tarefa para Concluir: ")
    for titulo, tarefa in tarefas.items():
        if 'Titulo' in tarefa and selecionar_tarefa == tarefa['Titulo']:
            del tarefas[titulo]
            print("Parabéns. Tarefa Concluída!")
            return
    print("Tarefa Não Encontrada.")