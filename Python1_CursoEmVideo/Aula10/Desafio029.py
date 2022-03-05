v = int(input('Digite a velocidade do carro em km/h: '))

if v > 80:
    print('Você foi multado! O valor da sua multa é R$ {}!'.format((v-80)*7))
else:
    print('Velocidade dentro do permitido!')