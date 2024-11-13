precos = [float(input(f"Digite o preço do produto {i+1}: R$")) for i in range(8)]
print(f"Maior preço: R${max(precos):.2f}")
print(f"Menor preço: R${min(precos):.2f}")
