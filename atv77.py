algoritmo "nomes_invertidos"
inicio
   vetor nomes[7]
   
   // Leitura dos 7 nomes
   para i de 1 até 7 passo 1 faça
      escreva("Digite o nome ", i, ": ")
      leia(nomes[i])
   fimpara

   // Mostrando os nomes na ordem inversa
   escreva("Nomes na ordem inversa: ")
   para i de 7 até 1 passo -1 faça
      escreva(nomes[i], " ")
   fimpara
fimalgoritmo
