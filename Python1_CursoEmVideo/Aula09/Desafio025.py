# Lê o nome de uma pessoa e retorna se contém "Silva"
nome = input('Digite o seu nome: ').upper()
print(bool(nome.find('SILVA') != -1))