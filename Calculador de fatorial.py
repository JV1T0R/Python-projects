n = int(input("Insira um número para calcular seu fatorial: "))

if n < 0:
    print("Não existe fatorial para o número inserido.")
    
elif n == 0 or n == 1:
    print("O fatorial do número inserido é: 1")

else:
    fat = n
    for x in range(n -1, 1, -1):
        fat = fat * x 
    print("O fatorial do número inserido é: {}".format(fat))
