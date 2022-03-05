#Retornar perímetro e área de um quadrado
#Valor do lado informado pelo usuário em centímetros
#Variável x corresponde ao perímetro e variável y corresponde a área

lado = int(input("Digite o tamanho do lado do quadrado em cm: "))
x = lado * 4
y = lado ** 2

print("\nperímetro:",x,"- área:",y)