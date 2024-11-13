maior_idade = 0
quantidade_homens = 0
idade_mulher_mais_jovem = float('inf')
soma_idades_homens = 0
total_homens = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    
    if idade > maior_idade:
        maior_idade = idade

    if sexo == 'M':
        quantidade_homens += 1
        soma_idades_homens += idade
        total_homens += 1
    elif sexo == 'F':
        if idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade
    
    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar != 'S':
        break

media_idade_homens = soma_idades_homens / total_homens if total_homens > 0 else 0

print(f"A maior idade lida: {maior_idade}")
print(f"Quantidade de homens cadastrados: {quantidade_homens}")
print(f"A idade da mulher mais jovem: {idade_mulher_mais_jovem}")
print(f"Média de idade entre os homens: {media_idade_homens:.2f}")
