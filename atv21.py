ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano BISSEXTO.")
else:
    print(f"{ano} não é um ano BISSEXTO.")

Digite um ano: 
1980
1980 é um ano BISSEXTO.


** Process exited - Return Code: 0 **
Press Enter to exit terminal
