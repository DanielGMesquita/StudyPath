# Calcular média de notas dos alunos

c = 0
s = 0

a = int(input('Quantos alunos tem a turma: '))

while c in range(0, a):
    aluno = input('\nQual o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    s = s + nota
    c = c + 1

m = s / a
print('A média das notas dos {} alunos é {}.'.format(a, m))