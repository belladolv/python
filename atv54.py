peso_mais_90kg = 0
menor_50kg_menor_160m = 0
mais_190m_mais_100kg = 0
soma_alturas = 0

for i in range(7):
    peso = float(input(f"Digite o peso da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    
    soma_alturas += altura
    
    if peso > 90:
        peso_mais_90kg += 1
    if peso < 50 and altura < 1.60:
        menor_50kg_menor_160m += 1
    if altura > 1.90 and peso > 100:
        mais_190m_mais_100kg += 1

media_altura = soma_alturas / 7
print(f"Média de altura do grupo: {media_altura:.2f}")
print(f"Pessoas com mais de 90kg: {peso_mais_90kg}")
print(f"Pessoas com menos de 50kg e menos de 1.60m: {menor_50kg_menor_160m}")
print(f"Pessoas com mais de 1.90m e mais de 100kg: {mais_190m_mais_100kg}")
