nome = input("Qual o seu nome? ")
sexo = input("Qual o seu sexo (M/F)? ").upper()
valor_compras = float(input("Qual o valor das suas compras? R$"))

if sexo == "F":
    desconto = 0.13
    print(f"Você é mulher, então o desconto é de 13%.")
else:
    desconto = 0.05
    print(f"Você é homem, então o desconto é de 5%.")

valor_com_desconto = valor_compras * (1 - desconto)
print(f"Valor com desconto: R${valor_com_desconto:.2f}")

Qual o seu nome? 
bella
Qual o seu sexo (M/F)? 
f
Qual o valor das suas compras? R$
700
Você é mulher, então o desconto é de 13%.
Valor com desconto: R$609.00


** Process exited - Return Code: 0 **
Press Enter to exit terminal
