# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

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
