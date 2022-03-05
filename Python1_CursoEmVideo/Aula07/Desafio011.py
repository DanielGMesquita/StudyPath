#Calcular área de uma parede com base nas informações de altura e largura
#Calcular quantos litros de tinta são necessários para pintar a parede

a = float(input('Digite a altura da parece em metros: '))
l = float(input('Digite a largura da parede em metros: '))

ar = a * l
ln = ar / 2

print('A parede tem área de {:.0f}m2 e a quantidade de litros necessários para pintar é {:.1f}'.format(ar, ln))