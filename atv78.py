algoritmo "vetor_multiplos_de_10"
inicio
   vetor numeros[15]
   vetor multiplosDe10[15]
   contador <- 0
   
   // Leitura dos 15 números
   para i de 1 até 15 passo 1 faça
      escreva("Digite o ", i, "º número: ")
      leia(numeros[i])
   fimpara

   // Mostrando os números e os múltiplos de 10
   escreva("Vetor completo: ")
   para i de 1 até 15 passo 1 faça
      escreva(numeros[i], " ")
      se numeros[i] % 10 = 0 então
         multiplosDe10[contador] <- numeros[i]
         contador <- contador + 1
      fimse
   fimpara
   
   // Mostrando os múltiplos de 10
   escreva("\nPosições dos múltiplos de 10: ")
   para i de 0 até contador-1 passo 1 faça
      escreva(multiplosDe10[i], " ")
   fimpara
fimalgoritmo
