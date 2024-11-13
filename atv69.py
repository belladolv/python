# Solicita ao usuário o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))

# Inicializa o termo atual
termo_atual = primeiro_termo

# Variável para armazenar a soma dos termos
soma = 0

# Exibe os 10 primeiros termos da PA e soma-os
print("Os 10 primeiros termos da PA são:")
for i in range(10):
    print(termo_atual, end=" ")
    soma += termo_atual
    termo_atual += razão

# Exibe a soma dos 10 primeiros termos
print(f"\nA soma dos 10 primeiros termos é: {soma}")
