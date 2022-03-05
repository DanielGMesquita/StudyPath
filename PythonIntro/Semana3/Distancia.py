# Calcular a distância entre dois pontos em um plano cartesiano de acordo com as coordenadas informadas pelo usuário
import math

print('Digite as coordenadas do primeiro ponto')
x1 = float(input('Digite o x:'))
y1 = float(input('Digite o y:'))

print('Digite as coordenadas do segundo ponto')
x2 = float(input('Digite o x: '))
y2 = float(input('Digite o y: '))

d = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

if d >= 10:
    print('longe')
else:
    print('perto')