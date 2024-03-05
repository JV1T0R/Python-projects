soma = 1 
antecec = 1
atual = 1
prox = antecec + atual
soma += prox
print ("{}, {}".format(antecec, atual))

while soma < 580:
    antecec = atual
    atual = prox
    prox = antecec + atual
    soma += prox
    print("{}".format(prox))
