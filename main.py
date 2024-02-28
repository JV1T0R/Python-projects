from functions import criador_de_tarefas
from functions import visualizador_de_tarefas
from functions import concluidor_de_tarefas

tarefas = {}

while True:
    print('''    GERENCIADOR DE TAREFAS
    [1] Adicionar Tarefa
    [2] Listar Tarefas
    [3] Concluir tarefas
    [4] Sair''')
    opcao = int(input("insira o número da opção para executa-la: "))

    if opcao == 1:
        nova_tarefa = criador_de_tarefas.criar_tarefa(tarefas)

    elif opcao == 2:
        while True:
            print(f"""                  [1] Ver Todas as Tarefas
                  [2] Filtrar por Prioridade
                  [3] Filtrar po Categoria
                  [4] Voltar ao Menu Principal""")
            opcao_de_vizualizacao = int(input("insira o número da opção para executa-la: "))

            if opcao_de_vizualizacao == 1:
                visualizador_de_tarefas.visualizar_todas_tarefas(tarefas)

            elif opcao_de_vizualizacao == 2:
                visualizador_de_tarefas.filtrar_tarefas_prioridade(tarefas)

            elif opcao_de_vizualizacao == 3:
                visualizador_de_tarefas.filtrar_tarefas_categaoria(tarefas)

            elif opcao_de_vizualizacao == 4:
                break

            else:
                print("Opção Invalida")

    elif opcao == 3:
        concluidor_de_tarefas.concluir_tarefa(tarefas)

    elif opcao == 4:
        print("sistema Encerrado.")
        break

    else:
        print("Opção Invalida")