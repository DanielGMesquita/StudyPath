n = int(input("Digite o primeiro número: "))
n1 = n
n = 1
fat = 1

while n <= n1:
    fat = fat * n
    n = n + 1

print(fat)