def Maior(a, b, c):
    return max(a, b, c)

# Leitura dos dados
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Chamada da função e exibição do resultado
maior = Maior(a, b, c)
print(f"O maior valor é: {maior}")
