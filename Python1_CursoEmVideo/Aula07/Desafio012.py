#Calcular descontos de um produto

p = float(input('Digite o preço: '))
print('O preço atual do produto é R${:.2f}'.format(p))
d = float(input('Digite quantos % de desconto deseja aplicar no produto: '))
np = p * (1-(d/100))
print('O novo preço do produto é R${:.2f}'.format(np))

