horas_atividade = float(input("Quantas horas de atividade física você fez no mês? "))

if horas_atividade <= 10:
    pontos = horas_atividade * 2
elif 10 < horas_atividade <= 20:
    pontos = horas_atividade * 5
else:
    pontos = horas_atividade * 10

dinheiro = pontos * 0.05
print(f"Você ganhou {pontos} pontos e R${dinheiro:.2f}.")
