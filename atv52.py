idades = [int(input(f"Digite a idade da pessoa {i+1}: ")) for i in range(10)]
media_idade = sum(idades) / len(idades)
mais_de_18 = sum(1 for idade in idades if idade > 18)
menos_de_5 = sum(1 for idade in idades if idade < 5)
maior_idade = max(idades)

print(f"Média de idade: {media_idade:.2f}")
print(f"Pessoas com mais de 18 anos: {mais_de_18}")
print(f"Pessoas com menos de 5 anos: {menos_de_5}")
print(f"A maior idade: {maior_idade}")
