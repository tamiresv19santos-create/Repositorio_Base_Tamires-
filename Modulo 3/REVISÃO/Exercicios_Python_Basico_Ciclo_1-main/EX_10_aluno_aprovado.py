# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nota1= int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota:"))

media1 = nota1 / 2
avaliacao = "reprovado"

if media1 >= 6:
    avaliacao="aprovado"

# ---------------------------------------------- -----------------------------------------------------------

segunda_nota1 = int(input("Digite sua primeira nota:"))
segunda_nota2 = int(input("Digite sua segunda nota:"))

soma2 = segunda_nota1 + segunda_nota2

media2 = soma2/ 2 
avaliacao2= "reprovado"

if media2 >= 6:
    avaliacao2="aprovado"

# ---------------------------------------------- -----------------------------------------------------------

print(f"Na primeira prova você tirou: {media1} e foi {avaliacao}")
print(f"Na segunda prova você tirou: {media2} e foi {avaliacao2}")





