#Sorteando um item na lista de 4 alunos para apagar o quadro
from random import choice
alunos = []
a1 = alunos.append(input('Digite o nome do aluno 1: '))
a2 = alunos.append(input('Digite o nome do aluno 2: '))
a3 = alunos.append(input('Digite o nome do aluno 3: '))
a4 = alunos.append(input('Digite o nome do aluno 4: '))

sort = choice(alunos)

print('O aluno sorteado é {}'.format(sort))