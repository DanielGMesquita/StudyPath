# Ler um número n de 0 a 9999 e imprime cada um dos dígitos separados
n = input('Digite um número: ')
n = list(n)
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(n[3], n[2], n[1], n[0]))
