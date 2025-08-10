#Construa um algoritmo que receba as duas médias bimestrais obtidas por um aluno durante o semestre. Ao final deve ser mostrada sua média semestral (aritmética) e a sua situação de acordo com a tabela, a seguir.

nota_primeiro_bimestre = float(input("Digite a nota do primeiro bimestre: "))
nota_segundo_bimestre = float(input("Digite a nota do segundo bimestre: "))

media_semestral = (nota_primeiro_bimestre + nota_segundo_bimestre) / 2

if (media_semestral>=6):
    print("Aprovado")
else:
    print("Reprovado")    