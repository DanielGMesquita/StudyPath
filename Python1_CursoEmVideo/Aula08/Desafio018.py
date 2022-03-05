# Ler um ângulo e retornar o seno, o cosseno e a tangente
# Angulo precisa ser convertido de graus para radianos
from math import radians, sin, cos, tan
angulo = radians(float(input('Digite um ângulo: ')))
sen = sin(angulo)
cos = cos(angulo)
tng = tan(angulo)

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tng))