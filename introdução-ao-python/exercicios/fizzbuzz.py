#Exercícios 4 - FizzBuzz parcial, parte 3
#Receba um número inteiro na entrada e imprima

#FizzBuzz

#na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.


numero = int(input('Digite um inteiro: '))

if not (numero%5&3) :
    print("É múltiplo de 3 e 5")
else:
    print("Não é múltiplo de 3 e 5")