l1 = int(input('Digite o comprimento da reta: '))
l2 = int(input('Digite o comprimento da reta: '))
l3 = int(input('Digite o comprimento da reta: '))

if (l1+l2 > l3) and (l2+l3 > l1) and (l3+l1 > l2):
    print('Pode formar um triangulo')
else:
    print('Não forma triangulo')