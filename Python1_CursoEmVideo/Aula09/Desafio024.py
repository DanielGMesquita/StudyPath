# Lê o nome de uma cidade e retorna se começa com a palavra "Santo"
cidade = input('Digite o nome da cidade: ').upper()
cidade = cidade.split()
print(bool(cidade[0]=='SANTO'))