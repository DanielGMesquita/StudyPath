#Calcular salário com aumento

s = float(input('Digite o salário atual: '))
ns = s * 1.15

print('O salário atual é de R${}, com o aumento de 15% irá para R${:.2f}'.format(s, ns))