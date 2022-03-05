#Retornar se número inteiro inserido pelo usuário é par ou ímpar
print('------PAR OU ÍMPAR---------')
n = int(input('Digite um número: '))

if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))