#Retorna o dígito da dezena de um número escolhido pelo usuário

num = int(input("Digite um número inteiro: "))
d = int((num // 10) % 10)

print("\nO dígito das dezenas é",d)