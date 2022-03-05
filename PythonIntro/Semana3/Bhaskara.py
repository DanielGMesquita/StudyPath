#Calcular o x de uma equação de segundo grau
#Se o delta for negativo - não tem raízes reais
#Se o delta for positivo - tem duas raízes reais
#Se o delta for zero - tem uma raíz reais
#Caso possua duas raízes, retornar em ordem crescente
import math

print('Insira os coeficientes:')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)
print('O delta da equação é {}'.format(delta))

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    x = ((b * -1) + math.sqrt(delta))/(2 * a)
    y = ((b * -1) - math.sqrt(delta))/(2 * a)
    if delta == 0:
        print('a raiz dupla desta equação é', x)
    else:
        if x > y:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(y, x))
        else:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x, y))



