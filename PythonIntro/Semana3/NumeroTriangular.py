#Verificar se o número selecionado pelo usuário é triangular (produto de 3 números inteiros consecutivos)
n = int(input('Digite um número para verificação:'))

c = 0
q = (c-2) * (c-1) * c

while q < n:
    q = (c - 2) * (c - 1) * c
    c = c + 1
    if q == n:
        print('O número resultado da multiplicação {} * {} * {} é triangular'.format((c-2), (c-1), c))
if q != n:
    print('Não triangular')