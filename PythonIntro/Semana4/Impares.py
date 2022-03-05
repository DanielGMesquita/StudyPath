# Receba um valor n e imprima os n primeiros números ímpares naturais
n = int(input('Digite um número: '))
c = 0  # contador para apoiar o laço de repetição
i = 1  # variável inicial para definir primeiro número a ser avaliado

while c < n:
    if i % 2 != 0:
        print(i)
        c = c + 1
        i = i + 1
    else:
        c = c + 0
        i = i + 1
