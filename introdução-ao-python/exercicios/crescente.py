#Exercício 5 - Verificando ordenação
# Receba 3 números inteiros na entrada e imprima

# crescente

#se eles forem dados em ordem crescente. Caso contrário, imprima 

#não está em ordem crescente

n1=int(input("Digite número 01:"))
n2=int(input("Digite número 02:"))
n3=int(input("Digite número 03:"))

if (n1 < n2 and n2 < n3):
    print("Está em ordem crescente")
else:
    print("Não está em ordem crescente")
   