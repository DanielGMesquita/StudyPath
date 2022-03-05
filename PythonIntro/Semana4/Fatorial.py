#Calcular fatorial de um número definido pelo usuário
n = int(input('Digite um número para calcular o fatorial: '))
c = 1  # contador para suportar o laço de repetição
fat = n  # valor inicial para dar suporte ao cálculo do fatorial
if n == 0:
    fat = 1
    print(fat)
else:
    while c < n:
        fat = fat * (n-c)
        c = c + 1
    print(fat)
