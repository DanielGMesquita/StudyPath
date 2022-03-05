#Sala de espera com decisões encadeadas
#65 anos ou mais - prioridades
#doenças infectocontagiosas - sala amarela

nome = input('Digite o nome do paciente: ')
idade = int(input('Digite a idade do paciente: '))
doenca_infecto = input('O paciente possui doença infectocontagiosa [SIM OU NÃO]: ').upper()

if idade >= 65:
    print('Paciente COM prioridade')
    if doenca_infecto == 'SIM':
        print('Direcione o paciente para a sala AMARELA')
    else:
        print('Direcione o paciente para a sala BRANCA')

if idade < 65:
    print('Paciente SEM prioridade')
    if doenca_infecto == 'NÃO':
        print('Direcione o paciente para a sala BRANCA')
    else:
        print('Direcione o paciente para a sala AMARELA')