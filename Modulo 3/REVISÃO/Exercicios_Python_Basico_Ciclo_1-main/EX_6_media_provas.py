# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7.0
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = print("Digite o nome do aluno:")
prova1 = float(input("Digite a nota da primeira prova:"))
prova2 = float(input("Digite a nota da seginda prova:"))
prova3 = float(input("Digite a nota da terceira prova:"))

soma = prova1 + prova2 + prova3
media = soma / 3




print(" --------------------------------------")
print("SISTEMA DE PROVAS")
print(" --------------------------------------")
print(f"Nome do aluno: {nome}")
print(f"Nota da primeira prova: {prova1}")
print(f"Nota da segunda prova: {prova2}")
print(f"Nota da terceira prova: {prova3}")

if media >=6:
    print("Você foi aprovado")

else:
    print("Você foi reprovado")


print(" ______________________________")
print(f"Aluno:{nome}")
print(f"media: {media}")
print(f" ______________________________")
