salario = float(input("Digite o salário atual: R$"))
genero = input("Digite o gênero do funcionário (M/F): ").upper()
anos_empresa = int(input("Quantos anos o funcionário trabalha na empresa? "))

if genero == "F":
    if anos_empresa < 15:
        aumento = 0.05
    elif 15 <= anos_empresa <= 20:
        aumento = 0.12
    else:
        aumento = 0.23
else:  # Homem
    if anos_empresa < 20:
        aumento = 0.03
    elif 20 <= anos_empresa <= 30:
        aumento = 0.13
    else:
        aumento = 0.25

novo_salario = salario * (1 + aumento)
print(f"O novo salário do funcionário é R${novo_salario:.2f}")

