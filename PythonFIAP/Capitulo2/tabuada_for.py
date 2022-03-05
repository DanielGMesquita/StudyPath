numero=int(input('Digite o número que você deseja ver a tabuada: '))
print("Tabuada de ",numero)
for mult in range(1,11,1):
    print(str(numero),'  X  ',str(mult),'  =  ',mult*numero)