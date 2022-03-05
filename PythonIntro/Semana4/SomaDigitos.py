# Receber um número inteiro n de entrada e calcular a soma dos seus dígitos

n = input('Digite um número inteiro: ')
s = 0  # variável de soma
c = 0  # contador para apoiar o laço de repetição

while c in range(0, len(n)):
    s = s + int(n[c])
    c = c + 1

print(s)