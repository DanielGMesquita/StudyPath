def maior_elemento(lista):
    maior = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior