#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de kms rodados: '))
d = int(input('Digite a quantidade de dias utilizados: '))

p = 60*d + 0.15*km

print('O cliente rodou {}km durante {} dias, totalizando R${:.2f} pelo aluguel'.format(km, d, p))