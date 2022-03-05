#Dados sobre o nome
nome = input('Digite seu nome completo: ')

# Nome com todas letras maiúsculas
print(nome.upper())

# Nome com todas letras minúsculas
print(nome.lower())

# Quantas letras sem espaçoes
print(len("".join(nome.split())))

# Quantas letras tem o primeiro nome
print(len(nome.split()[0]))

