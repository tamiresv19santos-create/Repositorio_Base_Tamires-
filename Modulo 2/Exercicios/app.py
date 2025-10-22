#calcular media escolar

nota1 = float(input("Digite a sua nota do primeiro bimestre:"))
nota2 = float(input("Digite a sua nota do segundo bimestre:"))
nota3 = float(input("Digite a sua nota do terceiro bimestre:"))
nota4 = float(input("Digite a sua nota do quarto bimestre:"))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

if media >= 7.0:
    print("Parabéns, você foi aprovado(a) ✅")

elif media >= 5.0 and media < 7.0:
    print("Você está de recuperação! ⚠️")

elif media < 5.0:
    print("Você foi reprovado❌")                 

else:
   print("Digite somente números!!")