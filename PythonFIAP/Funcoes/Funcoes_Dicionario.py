def perguntar():
    resposta = input("\nO que deseja realizar?"
                  +
                  "\n<I> para inserir usuário"
                  +
                  "\n<P> para pesquisar usuário"
                  +
                  "\n<E> para excluir usário"
                  +
                  "\n<L> para listar usuário"
                  +
                  "\nDigite aqui: ").upper()
    return resposta

def inserir(dicionario):
        dicionario[input("\nDigite o código único de acesso:  ").upper()] = [input("\nDigite o login do usuário: "),
                                                input("Digite o nome: ").upper(),
                                                input("Digite a última data de acesso: "),
                                                input("Digite a hora de acesso: "),
                                                input("Digite a última estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print('\nCod. Acesso......:', chave)
        print("Login............:", lista[0])
        print("Nome.............:", lista[1])
        print("Último acesso....:", lista[2])
        print('Horário de acesso:', lista[3])
        print("Última estação:..:", lista[4])

def excluir(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Objeto deletado")

def lista(dicionario):
    for chave, valor in dicionario.items():
        print("\nObjeto........")
        print("Login..........:", chave)
        print("Dados..........:", valor)