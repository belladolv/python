numero = int(input("Digite um valor: "))
print("Contagem:", end=" ")
for i in range(0, numero + 1):
    print(i, end=", " if i != numero else " ")
print("FIM!")
