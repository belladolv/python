algoritmo "notas_alunos"
inicio
   vetor notas[10]
   somaNotas <- 0
   maiorNota <- 0
   posMaiorNota[10] <- 0
   contadorAcimaMedia <- 0
   
   // Leitura das notas
   para i de 1 até 10 passo 1 faça
      escreva("Digite a nota do ", i, "º aluno: ")
      leia(notas[i])
      somaNotas <- somaNotas + notas[i]
      
      // Encontrando a maior nota
      se notas[i] > maiorNota então
         maiorNota <- notas[i]
      fimse
   fimpara

   // Calculando a média da turma
   mediaTurma <- somaNotas / 10

   // Contando alunos acima da média
   para i de 1 até 10 passo 1 faça
      se notas[i] > mediaTurma então
         contadorAcimaMedia <- contadorAcimaMedia + 1
      fimse
   fimpara

   // Mostrando os resultados
   escreva("Média da turma: ", mediaTurma, "\n")
   escreva("Alunos acima da média: ", contadorAcimaMedia, "\n")
   escreva("Maior nota: ", maiorNota, "\n")

   // Mostrando posições da maior nota
   escreva("Posições da maior nota: ")
   para i de 1 até 10 passo 1 faça
      se notas[i] = maiorNota então
         escreva(i, " ")
      fimse
   fimpara
fimalgoritmo
