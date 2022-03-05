#Programa Sala de Espera de Hospital
#pacientes com doenças infecto vão para sala amarela, demais para sala branca
#pacientes com mais de 65 anos tem prioridade
#identificar o direcionamento do paciente selecionado

nome = input('Digite o nome do paciente: ')
idade = int(input('Digite a idade do paciente: '))
doenca_infecto = input('O paciente possui doença infectocontagiosa [SIM OU NÃO]: ').upper()

if idade >= 65 and doenca_infecto == "SIM":
    print('O paciente será direcionado para a sala AMARELA - COM PRIORIDADE.')
elif idade >= 65 and doenca_infecto == "NÃO":
    print('O paciente será direcionada para a sala BRANCA - COM PRIORIDADE')
elif idade < 65 and doenca_infecto == "SIM":
    print('O paciente será direcionado para a sala AMARELA - SEM PRIORIDADE')
elif idade < 65 and doenca_infecto == "NÃO":
    print('O paciente será direcionada para a sala BRANCA - SEM PRIORIDADE')