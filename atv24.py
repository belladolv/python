distancia = float(input("Qual a distância da viagem em Km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da passagem é R${preco:.2f}")

Qual a distância da viagem em Km? 
600
O preço da passagem é R$270.00


** Process exited - Return Code: 0 **
Press Enter to exit terminal
