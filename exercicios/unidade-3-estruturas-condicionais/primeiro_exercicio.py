#Escreva um algoritmo que receba um número inteiro e diga se este é par ou ímpar.

par_ou_impar = float(input("Digite um número para saber se é par ou ímpar: "))

if (par_ou_impar % 2) == 0:
    print(f"O Número {par_ou_impar} é par!")
else:
    print("Ímpar")    