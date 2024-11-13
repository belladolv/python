def SuperSomador(a, b):
    return sum(range(a, b+1))

# Leitura dos dados
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

# Chamada da função e exibição do resultado
resultado = SuperSomador(a, b)
print(f"A soma de todos os valores entre {a} e {b} é {resultado}")
