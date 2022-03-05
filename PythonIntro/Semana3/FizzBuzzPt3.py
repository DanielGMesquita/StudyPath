#Receba um número inteiro na entrada e imprima FizzBuzz se o número for divisível por 3 e 5.
#Caso contrário, imprima o mesmo número que foi dado na entrada.

n = int(input('Digite um número inteiro: '))

if n % 3 == 0 and n % 5 ==0:
    print('FizzBuzz')
else:
    print(n)