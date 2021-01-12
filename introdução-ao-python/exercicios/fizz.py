#Receba um número inteiro na entrada e imprima 

#Fizz

 #se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Digite um inteiro: '))

if not (numero%3) :
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")