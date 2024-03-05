valor_final = 0.1

while valor_final != 0:
    print("Digite 0 para encerrar")

    if valor_final == 0:
        print("ENCERRADO")

    else:
        valor_final = float(input("Insira o valor final do produto para remover o valor do IPI: "))

        IPI = 1.065

        valor_inicial = valor_final/IPI

        print(f"Valor inicial: {round(valor_inicial,2)}")
        print("")
        print("")
