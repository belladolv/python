inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o último valor: "))
incremento = int(input("Digite o incremento: "))

if inicio < fim:
    for i in range(inicio, fim + 1, incremento):
        print(i, end=" ")
else:
    for i in range(inicio, fim - 1, -incremento):
        print(i, end=" ")
print("Acabou!")
