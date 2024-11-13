a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("O triângulo é ISÓSCELES.")
    else:
        print("O triângulo é ESCALENO.")
else:
    print("Esses segmentos NÃO podem formar um triângulo.")
