import random

#Computador escolhe número aleatório entre 1 e 5
x = random.randrange(1, 6)

#Usuário digita número para tentar adivinhar
n = int(input('Tente adivinhar o número entre 1 a 5 escolhido pelo computador:'))

if n == x:
    print('Parabéns! Você acertou! O número escolhido pelo computador foi {}'.format(x))
else:
    print('Você errou! O número escolhido pelo computador foi {}'.format(x))