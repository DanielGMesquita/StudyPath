#sortear a ordem de 4 alunos para apresentação de um trabalho
from random import shuffle
alunos = []
a1 = alunos.append(input('Digite o nome do aluno 1: '))
a2 = alunos.append(input('Digite o nome do aluno 2: '))
a3 = alunos.append(input('Digite o nome do aluno 3: '))
a4 = alunos.append(input('Digite o nome do aluno 4: '))
shuffle(alunos)

print('A ordem da apresentação será: ')
print(alunos)