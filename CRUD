import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2803',
    database='python CRUD',
)
cursor = conexao.cursor()

print("Bem vindo ao cadastro de alunos!")

opcao = 0

while opcao != 5:
    print('''    [1] Create
    [2] Read
    [3] Update
    [4] Delete
    [5] Exit''')
    opcao = int(input("insira o número da opção para executa-la: "))

    # [1] Create: inserts an element into the table.
    if opcao == 1:
        print("Novo cadstro:")
        nome = str(input("Insira o nome do aluno a ser cadastrado: "))
        matricula = int(input("Insira a matrícula do aluno a ser cadastrado: "))
        seleciona = f'SELECT matricula FROM alunos WHERE matricula = {matricula}'
        cursor.execute(seleciona)
        resultado = cursor.fetchall()

        if len(resultado) != 0:
            print('A matrícula inserida já existe no cadastro.\n')

        else:
            insert = f'INSERT INTO alunos (nome, matricula) VALUES ("{nome}", {matricula})'
            cursor.execute(insert)
            conexao.commit()
            print("Cadastro realizado com sucesso!\n")

    # [2] Read: Shows the table content.
    elif opcao == 2:
        read = f'SELECT * FROM alunos'
        cursor.execute(read)
        cadastros = cursor.fetchall()
        print(f'CADASTROS:\n{cadastros}\n')

    # [3] Update: changes a name from the column nome.
    elif opcao == 3:
        print("Atualização de cadstro:")
        matricula = int(input("Insira a matrícula do aluno a ter o cadastro alterado: "))
        nome = str(input("Insira o novo nome do a ser inserido no cadastro: "))
        update = f'UPDATE alunos SET nome = "{nome}" WHERE matricula = {matricula}'
        cursor.execute(update)
        conexao.commit()
        print("Cadastro atualizado com sucesso!\n")

    # [4] Delete: deletes an element from the table.
    elif opcao == 4:
        print("Remoção de cadastro:")
        matricula = int(input("Insira a matrícula do aluno a ser apagado do cadstro: "))
        delete = f'DELETE FROM alunos WHERE matricula = "{matricula}"'
        cursor.execute(delete)
        conexao.commit()
        print("Cadastro deletado com sucesso!\n")

    # [5] Exit: finishes the program.
    elif opcao == 5:
        print("encerrando cadastro...")

    # Shows if an invalid option was typed.
    else:
        print("Opção inválida. Tente novamente.")

cursor.close()
conexao.close()
