soma = 0
while True:
    numero = int(input("Digite um número (1111 para parar): "))
    if numero == 1111:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")
