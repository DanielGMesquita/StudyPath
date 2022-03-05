#Lista de equipamentos e características
#Inclui depreciação de 10% em equipamento selecionado
#Deleta equipamento defeituoso com base no serial number
#Retorna características de um item selecionado pelo usuário

equipamentos = []
valores = []
serial = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    serial.append(int(input("Serial Number: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite "+"S"+" para continuar").upper()

deletar = int(input("Digite o serial number a ser deletado: "))
for indice in range(0, len(departamento)):
    if serial[indice] == deletar:
        del departamento[indice]
        del equipamentos[indice]
        del valores[indice]
        del serial[indice]
        break

res = "S"
while res == "S":
    depreciacao = input("Digite o nome do equipamento que sofrerá depreciação: ")
    for indice in range(0,len(equipamentos)):
        if depreciacao == equipamentos[indice]:
            print("Valor antigo: ",valores[indice])
            valores[indice] = valores[indice]*0.9
            print("Novo valor: ",valores[indice])
    res = input('Digite S para continuar').upper()

for indice in range(0,len(equipamentos)):
    print("Equipamento..: ",(indice+1))
    print("Nome............: ", equipamentos[indice])
    print("Valor...........: ", valores[indice])
    print("Serial..........: ", serial[indice])
    print("Departamento....: ", departamento[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor....: ", valores[indice])
        print("Serial...: ", serial[indice])

