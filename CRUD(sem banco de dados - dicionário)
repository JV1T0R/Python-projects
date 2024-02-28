print("Bem vindo ao sistema de cadastro de alunos!")

map_alunos = {}
opcao = 0

while opcao != 5:
    print('''    [1] Create
    [2] Read
    [3] Update
    [4] Delete
    [5] Save & Exit''')
    opcao = int(input("insira o número da opção para executa-la: "))

    # [1] Create: inserts an element into the list.
    if opcao == 1:
        print("")

        matricula = str(input("Insira a matrícula do aluno que deseja cadastrar: "))

        if matricula in map_alunos:
            print("Matrícula já existente.")
            continue

        nome = str(input("Insira o nome do aluno que deseja cadastrar: "))

        map_alunos[matricula] = {'matricula': matricula, 'nome': nome}

    # [2] Read: Shows the list.
    elif opcao == 2:
        print("")

        print("REGISTROS:")
        for aluno in map_alunos.values():
            print("Nome:", aluno['nome'], "/", "Matrícula:", aluno['matricula'])

    # [3] Update: changes a list element.
    elif opcao == 3:
        print("")

        matricula = str(input("Qual a mátricula do aluno a ter o cadstro atualizado: "))
        nome = ""

        if matricula in map_alunos:
            nome_new = str(input("Insira o novo nome a ser inserida no cadastro: "))

            map_alunos[nome] = {'matricula': matricula, 'nome': nome_new}
            del map_alunos[nome]
            continue

        print("A matrícula inserida não existe no cadastro,")


    # [4] Delete: erases an element of the list.
    elif opcao == 4:
        print("")

        matricula = str(input("Qual a matricula a ser apagada do cadastro? "))

        if matricula in map_alunos:
            del map_alunos[matricula]
            continue

        print("A matrícula inserida não existe no cadastro,")

    # [5] Save & Exit: closes the program and saves the current list to a txt document.
    elif opcao == 5:
        print("")

        stralunos = "REGISTROS:\n"
        for aluno in map_alunos.values():
            stralunos = stralunos + "Nome: " + aluno['nome'] + " / " + "Matrícula: " + aluno['matricula'] + "\n"
        arquivo = open("lista-alunos", "w")
        arquivo.write(stralunos)

        print("Salvando informações e encerrando o programa...")

    # Shows if an invalid option was typed.
    else:
        print("Opção inválida. Tente novamente.")
