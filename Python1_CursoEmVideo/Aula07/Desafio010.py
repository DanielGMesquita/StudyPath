#Conversor de dólar
#Formatação - .(x)f em que x é a quantidade de casas decimais flutuantes

r = int(input('Digite a quantidade de R$ que você tem: '))
d = r / 5.71
print('Você tem um total de R${:.2f} que equivale a US${:.2f}'.format(r, d))