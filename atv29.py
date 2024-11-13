nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual: R$"))
anos_trabalho = int(input("Quantos anos trabalha na empresa? "))

if anos_trabalho <= 3:
    aumento = 0.03
elif anos_trabalho <= 10:
    aumento = 0.125
else:
    aumento = 0.20

novo_salario = salario * (1 + aumento)
print(f"O novo salário de {nome} é R${novo_salario:.2f}")
