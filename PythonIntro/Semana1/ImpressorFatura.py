#Imprimir descrição de fatura de acordo com informações inseridas pelo usuário

print("--------------------------------")
print("Insira as informações do cliente")
print("--------------------------------")

nome = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

print("\nOlá,",nome)
print("A sua fatura com vencimento em",dia,"de",mes,"no valor de R$",valor,"está fechada.")