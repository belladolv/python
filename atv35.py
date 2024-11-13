tipo_carro = input("Digite o tipo de carro alugado (popular ou luxo): ").lower()
dias = int(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km foram percorridos? "))

if tipo_carro == "popular":
    aluguel_diario = 90
    if km <= 100:
        custo_km = km * 0.20
    else:
        custo_km = km * 0.10
elif tipo_carro == "luxo":
    aluguel_diario = 150
    if km <= 200:
        custo_km = km * 0.30
    else:
        custo_km = km * 0.25
else:
    print("Tipo de carro inválido!")
    exit()

total = aluguel_diario * dias + custo_km
print(f"Total a pagar: R${total:.2f}")
