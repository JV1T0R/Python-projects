def criar_tarefa(tarefas):
    print("")
    while True:
        try:
            titulo = input("Insira o Título da Tarefa: ").strip().lower()
            descricao = input("Descreva Breviamente a Tarefa: ").strip().lower()
            prioridade = input("Qual a Prioridade Desta tarefa? (Normal ou Urgente): ").strip().lower()
            categoria = input("Qual a categoria Desta tarefa? ").strip().lower()

            if not (titulo and descricao and prioridade and categoria):
                raise ValueError("Por favor, preencha todos os campos.")
            tarefas[titulo] = {'Título': titulo, 'Descrição': descricao, 'Prioridade': prioridade,
                               'Categoria': categoria}
            print("Tarefa criada com sucesso!\n")
            break

        except ValueError as error:
            print(error)


