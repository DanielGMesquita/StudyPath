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
    return lista






