total_salarios_homens = 0
total_salarios_mulheres = 0

while True:
    salario = float(input("Digite o salário do funcionário: R$"))
    sexo = input("Digite o sexo do funcionário (M/F): ").upper()

    if sexo == 'M':
        total_salarios_homens += salario
    elif sexo == 'F':
        total_salarios_mulheres += salario
    else:
        print("Sexo inválido! Digite 'M' para masculino ou 'F' para feminino.")
        continue

    continuar = input("Deseja continuar (S/N)? ").upper()
    if continuar != 'S':
        break

print(f"Total de salários pagos aos homens: R${total_salarios_homens:.2f}")
print(f"Total de salários pagos às mulheres: R${total_salarios_mulheres:.2f}")
