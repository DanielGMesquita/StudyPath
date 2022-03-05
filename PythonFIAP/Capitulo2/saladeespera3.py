#Sala de espera com decisões encadeadas
#65 anos ou mais e grávidas- prioridades, descartar mulheres menores que 10 anos da possibilidade
#doenças infectocontagiosas - sala amarela; outros para sala branca

nome = input('Digite o nome do paciente: ')
idade = int(input('Digite a idade do paciente: '))
doenca_infecto = input('O paciente possui doença infectocontagiosa [SIM OU NÃO]: ').upper()

#PROBLEMA 1
while doenca_infecto != "SIM" and doenca_infecto != "NÃO":
    print("Responda com SIM ou NÃO:")
    doenca_infecto = input('O paciente possui doença infectocontagiosa [SIM OU NÃO]: ').upper()

if doenca_infecto == "SIM":
    print('Paciente deve ser encaminhado(a) para a sala AMARELA')
else:
    print('Paciente deve ser encaminhado(a) para sala BRANCA')

#PROBLEMA 2
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input('Qual o sexo do paciente [M/F/NB]: ')
    if genero == "F" or genero == "NB" and idade > 10:
        gravidez = input('Paciente está gestante [SIM/NÃO]: ')
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print('Paciente SEM prioridade')
    else:
        print('Paciente SEM prioridade')