n = input('Digite um número maior que 0: ')
d = int(input('Digite o valor do dígito que deseja contar: '))

c = 0
cd = 0

for c in range(0, len(n)):
    if int(n[c]) // d == 1:
        cd = cd + 1

print('O número {} aparece {} vezes no número {}'.format(d, cd, n))
