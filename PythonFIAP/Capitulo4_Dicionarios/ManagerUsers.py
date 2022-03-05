from Funcoes.Funcoes_Dicionario import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios,input("\nQual número único de acesso deseja pesquisar?").upper())
    if opcao == "E":
        excluir(usuarios,input("\nQual usuário deseja excluir?").upper())
    if opcao == "L":
        lista(usuarios)

    opcao = perguntar()

