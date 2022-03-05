def remove_repetidos(lista):
    lista.sort()
    i = 0
    p = i + 1
    while i < len(lista):
        if lista[i] == lista[p]:
            del lista[p]
            i -= 1
            p = i - 1
        else:
            i += 1
            p = i - 1
    print(lista)

def soma_elementos(lista):
    soma = 0
    for i in range(0, len(lista)):
        soma = soma + lista[i]
    return soma

def maior_elemento(lista):
    maior = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

