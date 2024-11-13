a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

if a + b > c and a + c > b and b + c > a:
    print("Esses segmentos podem formar um triângulo.")
else:
    print("Esses segmentos NÃO podem formar um triângulo.")
