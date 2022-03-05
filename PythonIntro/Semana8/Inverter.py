lista = []
n = 1

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        lista.append(n)
clone = lista[::-1]
for i in range(0, len(clone)):
    print(clone[i])