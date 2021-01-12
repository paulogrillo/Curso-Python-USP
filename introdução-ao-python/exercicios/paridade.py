## Par Ou Impar?

# Nesta lista de exercícios vamos praticar os conceitos vistos até agora.  Cada exercício deve ser resolvido em um arquivo separado e a seguir  enviado através da web. A correção automática pode demorar alguns  minutos. Você pode submeter a mesma resposta mais de uma vez caso  perceba que a resposta anterior tinha algum problema; a última versão é a  que vale.

###Note que a correção verifica se o resultado corresponde (exatamente) ao que foi pedido no enunciado. Letras maiúsculas ou minúsculas, número de espaços e pontuação diferentes do pedido são tratados como erro.
#
#
# [Exercício] 1 - Par ou ímpar?
# Receba um número inteiro na entrada e imprima

# par 

# quando o número for par ou

# ímpar

# quando o número for ímpar.


numero = float(input('Digite um inteiro: '))
resto = numero % 2
if resto == 0:
    print("número é par")
else:
    print("número é impar")