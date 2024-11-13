algoritmo "vetor_chave_aleatoria"
inicio
   vetor numeros[30]
   chave <- 0
   contador <- 0
   
   // Preenchendo o vetor com números aleatórios entre 1 e 15
   para i de 1 até 30 passo 1 faça
      numeros[i] <- aleatorio(1, 15)
   fimpara

   // Mostrando os valores gerados
   escreva("Valores gerados: ")
   para i de 1 até 30 passo 1 faça
      escreva(numeros[i], " ")
   fimpara

   // Lendo a chave do usuário
   escreva("\nDigite a chave a ser pesquisada: ")
   leia(chave)

   // Contando as ocorrências da chave e mostrando as posições
   para i de 1 até 30 passo 1 faça
      se numeros[i] = chave então
         escreva("Chave encontrada na posição: ", i, " | ")
         contador <- contador + 1
      fimse
   fimpara

   // Mostrando a quantidade de vezes que a chave foi sorteada
   escreva("\nQuantidade de vezes que a chave foi sorteada: ", contador)
fimalgoritmo
