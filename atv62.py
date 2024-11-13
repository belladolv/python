quantidade_idades = 0
soma_idades = 0
quantidade_21_ou_mais = 0

faça_while = True
while faça_while:
    idade = int(input("Digite a idade: "))
    quantidade_idades += 1
    soma_idades += idade
    if idade >= 21:
        quantidade_21_ou_mais += 1
    
    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar != "S":
        faça_while = False

media_idades = soma_idades / quantidade_idades if quantidade_idades > 0 else 0

print(f"Quantidade de idades digitadas: {quantidade_idades}")
print(f"Média das idades: {media_idades:.2f}")
print(f"Quantidade de pessoas com 21 anos ou mais: {quantidade_21_ou_mais}")
