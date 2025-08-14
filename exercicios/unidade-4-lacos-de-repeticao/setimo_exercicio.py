#Anacleto tem 1,50 m de altura e cresce 2 cm por ano, enquanto Felisberto tem 1,10 m de altura e cresce 3 cm por ano. Construa um algoritmo que calcule e mostre quantos anos serão necessários para que Felisberto seja maior que Anacleto.

anacleto = 1.50
felizberto = 1.10
anos = 0

while anacleto>felizberto:
    anos += 1
    felizberto += 0.03
    anacleto += 0.02
print(f"Se passaram {anos} anos e Felizberto está com {felizberto:.2f}m e Anacleto com {anacleto:.2f}m")