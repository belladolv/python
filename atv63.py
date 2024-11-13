soma_valores = 0
quantidade_valores = 0
menor_valor = None
quantidade_pares = 0

faça_while = True
while faça_while:
    valor = int(input("Digite um número: "))
    soma_valores += valor
    quantidade_valores += 1
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
    if valor % 2 == 0:
        quantidade_pares += 1
    
    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar != 'S':
        faça_while = False

media_valores = soma_valores / quantidade_valores if quantidade_valores > 0 else 0

print(f"Soma dos valores: {soma_valores}")
print(f"Menor valor digitado: {menor_valor}")
print(f"Média dos valores: {media_valores:.2f}")
print(f"Quantidade de números pares: {quantidade_pares}")
