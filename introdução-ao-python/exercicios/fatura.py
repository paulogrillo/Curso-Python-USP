# Exercício 1
# Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

# 1 Olá, Fulano de Tal
# 2 A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

# Olá, Fulano de Tal
# A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
# Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

# Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

# Exemplo:

# Entrada de Dados:
# 1 Digite o nome do cliente: Fulano de Tal
# 2 Digite o dia de vencimento: 9
# 3 Digite o mês de vencimento: Janeiro
# 4 Digite o valor da fatura: 350,00

# Digite o nome do cliente: Fulano de Tal
# Digite o dia de vencimento: 9
# Digite o mês de vencimento: Janeiro
# Digite o valor da fatura: 350,00

# Saída de Dados:
# 1 Olá, Fulano de Tal
# 2 A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

nome = input("Digite o nome do cliente:")
diaVencimento = input("Digite o dia de vencimento:")
mesVencimento = input("Digite o mês de vencimento:")
valor = input("Digite o valor da fatura:")

print ("Olá, ", nome)
print ("A sua fatura com vencimento em", diaVencimento, "de", mesVencimento, "no valor de R$", valor, "está fechada.")