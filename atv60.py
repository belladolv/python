
nome_mais_velho = ""
nome_mulher_mais_jovem = ""
idade_mais_velha = -1
idade_mulher_mais_jovem = 999
soma_idades = 0
quantidade_pessoas = 0
quantidade_homens_30 = 0
quantidade_mulheres_18 = 0

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    # Acumulando somatório de idades e contando total de pessoas
    soma_idades += idade
    quantidade_pessoas += 1

    # Encontrar a pessoa mais velha
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

    # Encontrar a mulher mais jovem
    if sexo == 'F' and idade < idade_mulher_mais_jovem:
        idade_mulher_mais_jovem = idade
        nome_mulher_mais_jovem = nome

    # Contagem de homens com mais de 30 anos
    if sexo == 'M' and idade > 30:
        quantidade_homens_30 += 1

    # Contagem de mulheres com menos de 18 anos
    if sexo == 'F' and idade < 18:
        quantidade_mulheres_18 += 1

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar != 'S':
        break

# Exibindo resultados
media_idades = soma_idades / quantidade_pessoas if quantidade_pessoas > 0 else 0

print(f"Nome da pessoa mais velha: {nome_mais_velho}")
print(f"Nome da mulher mais jovem: {nome_mulher_mais_jovem}")
print(f"Média de idade do grupo: {media_idades:.2f}")
print(f"Homens com mais de 30 anos: {quantidade_homens_30}")
print(f"Mulheres com menos de 18 anos: {quantidade_mulheres_18}")
