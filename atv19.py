nome = input("Qual o nome do aluno? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A média de {nome} é {media:.2f}.")
if media >= 7:
    print("Bom aproveitamento!")
else:
    print("Não teve um bom aproveitamento.")

Qual o nome do aluno? 
izabella
Digite a primeira nota: 
8
Digite a segunda nota: 
7
A média de izabella é 7.50.
Bom aproveitamento!


** Process exited - Return Code: 0 **
Press Enter to exit terminal
