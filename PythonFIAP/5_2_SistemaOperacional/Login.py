import getpass

usuario = input('Digite o usuário: ').upper()
senha = getpass.getpass('Digite a senha: ')

if usuario == 'DGM' and senha == '12345':
    print('logado')
else:
    print('negado')