homens = 0
mulheres = 0
soma_idade_homens = 0
idade_mulher_mais_jovem = float('inf')
soma_idades = 0

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ").upper()
    
    soma_idades += idade
    
    if sexo == "M":
        homens += 1
        soma_idade_homens += idade
    else:
        mulheres += 1
        if idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade

media_idade = soma_idades / 5
media_idade_homens = soma_idade_homens / homens if homens > 0 else 0

print(f"Homens cadastrados: {homens}")
print(f"Mulheres cadastradas: {mulheres}")
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Média de idade dos homens: {media_idade_homens:.2f}")
print(f"A mulher mais jovem tem {idade_mulher_mais_jovem} anos.")
