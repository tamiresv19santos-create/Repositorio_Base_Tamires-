# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
desconto_porcentagem= int(input("Digite o desconto: "))

valor_desconto = valor * (desconto_porcentagem /  100 )
total_produto = valor - valor_desconto

print(f"Qual o preço do produto? {produto}")
print(f"Qual a porcentagem de desconto? {desconto_porcentagem}")
print(f" O produto que custa R${valor} terá R${valor_desconto} de desconto.")
print(f"Você pagara R${total_produto} no {produto}.")
