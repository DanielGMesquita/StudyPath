# Ler uma frase e mostrar informações
frase = str(input('Digite uma frase: ').upper()).strip()

# contar quantos A tem na frase
print('A quantidade de letras A é:',frase.count('A'))

# Em que posição a letra A aparece a primeira e última vez
print('A primeira posição do A é {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))