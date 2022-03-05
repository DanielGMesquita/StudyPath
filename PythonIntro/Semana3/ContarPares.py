r = 'S'
numeros = []

while r == 'S':
    numeros.append(int(input('Digite um número: ')))
    r = input('Para continuar digite "S":').upper()
p = 0
c = 0
while c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        p = p + 1
    c = c + 1

print('A lista de números selecionados possui {} pares'.format(p))
