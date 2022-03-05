# Lê um nome e imprime o primeiro e último nomes
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print(nome[0]+' '+nome[-1])