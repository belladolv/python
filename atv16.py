cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos que você já fuma: "))
minutos_perdidos_por_cigarro = 10
total_cigarros = cigarros_por_dia * anos_fumando * 365
total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro
dias_perdidos = total_minutos_perdidos / (24 * 60)
print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida devido ao fumo.")

Digite a quantidade de cigarros fumados por dia: 
8
Digite a quantidade de anos que você já fuma: 
17
Você perdeu aproximadamente 344.72 dias de vida devido ao fumo.


** Process exited - Return Code: 0 **
Press Enter to exit terminal
