#Converter temperatura em C para F

C = float(input('Digite a temperatura em ºC: '))
F = C * 9 / 5 + 32

print('A temperatura em {} ºC equivale a {} ºF'.format(C, F))