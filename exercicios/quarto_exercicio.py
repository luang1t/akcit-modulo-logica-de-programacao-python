#Escreva um algoritmo que leia o nome do aluno e as 4 notas bimestrais do ano, calcule e mostre o nome do aluno e as suas médias aritméticas anual e semestrais.
nome_aluno = str(input("Digite seu nome: "))
nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_terceira = float(input("Digite a terceira nota: "))
nota_quarta = float(input("Digite a quarta nota: "))

media_anual = (nota_um+nota_dois+nota_terceira+nota_quarta)/4
media_primeiro_bimestre = (nota_um+nota_dois)/2
media_segundo_bimestre = (nota_terceira+nota_quarta)/2

print(f"{nome_aluno} Bem vindo ao portal de notas:\nPrimeiro semestre: {nota_um}\nSegundo semestre: {nota_dois}\nTerceiro semestre: {nota_terceira}\nQuarto semestre: {nota_quarta}")
print(f"Suas médias:\nPrimeiro Bimestre media: {media_primeiro_bimestre: .2f}\nSegundo Bimestre media: {media_segundo_bimestre: .2f}\nMedia anual: {media_anual: .2f}")
