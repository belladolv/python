pares = 0
impares = 0
for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Ímpares: {impares}")
