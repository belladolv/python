quantidade_mulheres = 0
quantidade_homens_mais_100kg = 0
soma_peso_mulheres = 0
maior_peso_homem = 0

for i in range(8):
    sexo = input("Digite o sexo (M/F): ").upper()
    peso = float(input("Digite o peso: "))

    if sexo == 'F':
        quantidade_mulheres += 1
        soma_peso_mulheres += peso
    if sexo == 'M' and peso > 100:
        quantidade_homens_mais_100kg += 1
    if sexo == 'M' and peso > maior_peso_homem:
        maior_peso_homem = peso

media_peso_mulheres = soma_peso_mulheres / quantidade_mulheres if quantidade_mulheres > 0 else 0

print(f"Quantas mulheres cadastradas: {quantidade_mulheres}")
print(f"Quantos homens pesam mais de 100Kg: {quantidade_homens_mais_100kg}")
print(f"Média de peso entre as mulheres: {media_peso_mulheres:.2f}")
print(f"O maior peso entre os homens: {maior_peso_homem}")
