#Desafio de decisão
#Solicitar nível de acesso: ADM, USR ou GUEST
#Solicitar o gênero que o usuário se identifica: M (Masculino), F (Feminino)

acesso = input('Defina nível de acesso [ADM/USR/GUEST]: ').upper()

if acesso == "ADM" or acesso == "USR":
    genero = input('Qual o sexo do usuário(a) [F/M]: ').upper()
    if acesso == "ADM":
        if genero == "F":
            print('Olá administradora!')
        else:
            print('Olá administrador!')
    elif acesso == "USR":
        if genero == "F":
            print('Olá usuária!')
        else:
            print('Olá usuário!')
elif acesso == "GUEST":
    print("Olá visitante!")
else:
    print('Olá desconhecido(a)')