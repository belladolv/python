def Maior(a, b):
    if a > b:
        print(f"O maior valor é: {a}")
    elif b > a:
        print(f"O maior valor é: {b}")
    else:
        print("Os valores são iguais!")

# Leitura dos dados
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

# Chamada da função
Maior(a, b)
