# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias_rodados = int(input("DIgite quantos dias foram rodados com o carro:"))
km= int(input("Digite quantos kms foram rodados com o carro:"))

aluguel = 60 * dias_rodados
valor_km = 0.15 * km 

valor_total = (aluguel + valor_km)

print(f"Você andou {km}km por {dias_rodados} dias, então o preço que devera ser pago será R${valor_total:.2f}.")
