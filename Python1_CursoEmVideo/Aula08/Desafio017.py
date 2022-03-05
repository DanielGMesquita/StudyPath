#Ler o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo e retornar a hipotenusa
from math import hypot
o = float(input('Cateto oposto: '))
a = float(input('Cateto adjacente: '))

print('A hipotenusa do triângulo é {:.2f}'.format(hypot(o, a)))