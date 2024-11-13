def Potencia(base, expoente):
    return base ** expoente

# Leitura dos dados
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Chamada da função e exibição do resultado
resultado = Potencia(base, expoente)
print(f"O resultado de {base}^{expoente} é {resultado}")
