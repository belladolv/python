ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano BISSEXTO.")
else:
    print(f"{ano} não é um ano BISSEXTO.")