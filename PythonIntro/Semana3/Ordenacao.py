#Receba 3 números inteiros na entrada e imprima "crescente"
#se eles forem dados em ordem crescente. Caso contrário, imprima "não está em ordem crescente""

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b < c:
    print('Crescente')
else:
    print('Não está em ordem crescente')