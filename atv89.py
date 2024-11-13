def Gerador(mensagem, repeticoes, borda):
    if borda == 1:
        borda_str = "+-------=======------+"
    elif borda == 2:
        borda_str = "~~~:::::::~~"
    elif borda == 3:
        borda_str = "<<<<<<<<------->>>>>>"
    
    for _ in range(repeticoes):
        print(borda_str)
        print(mensagem)
        print(borda_str)

# Chamada da função
Gerador("Portugol Studio", 4, 2)
