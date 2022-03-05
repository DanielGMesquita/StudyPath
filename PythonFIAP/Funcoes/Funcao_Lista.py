def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input('Serial: ')),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite S se deseja continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("\nNome..........:",elemento[0])
        print("Valor.........:",elemento[1])
        print("Serial........:",elemento[2])
        print("Departamento..:",elemento[3])

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja informação: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor......: ",elemento[1])
            print("Serial.....: ",elemento[2])

#Depreciação com escolha do % pelo usuário e por produto
def depreciarPorNome(lista):
    eqp = input("\nDigite o nome do equipamento que sofrerá depreciação: ")
    dep = float(input("Digite o valor da depreciação: "))
    for elemento in lista:
        if eqp == elemento[0]:
            print("O valor antigo era: ",elemento[1])
            elemento[1] == (elemento[1]*dep)
            print("O novo valor é: ",elemento[1])

#Depreciação com valor fixo
def depreciarPorNome(lista,porc):
    eqp = input("\nDigite o nome do equipamento que sofrerá depreciação: ")
    for elemento in lista:
        if eqp == elemento[0]:
            print("O valor antigo era: ",elemento[1])
            elemento[1] == (elemento[1] * (1-porc/100))
            print("O novo valor é: ",elemento[1])

def excluirPorSerial(lista):
    serial = int(input("\nDigite o serial defeituoso a ser excluído: "))
    for elemento in lista:
        if serial==elemento[2]:
            lista.remove(elemento)
            return "Itens excluídos."

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("\nO maior valor entre os equipamentos é R$",max(valores))
        print("O menor valor entre os equipamentos é R$",min(valores))
        print("O valor total do inventário é R$",sum(valores))