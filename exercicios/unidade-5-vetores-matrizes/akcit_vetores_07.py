#Escreva um algoritmo que leia uma matriz G 5x5 e preencha automaticamente dois vetores, 
# de cinco elementos, SL e SC que contenham, respectivamente, as somas das linhas e das colunas da matriz G. 
# Ao final, escreva os valores dos vetores SL e SC.
from random import randint

matriz = []
SL = []
SC = []

for _ in range(0,5):
    matriz.append(list())

for linha in range(0,5):
    for coluna in range (0,5):
        while True:
            numero = randint(0,26)
            if any(numero in sub_linha for sub_linha in matriz):
                continue
            else:
                matriz[linha].append(numero)
                break

for prnt_linha in range(0,5):
    for prnt_coluna in range(0,5):
        print(f"[{matriz[prnt_linha][prnt_coluna]:^5}]", end = '')
    print()


for soma_linha in range(0,len(matriz)):
    soma = sum(matriz[soma_linha])
    SL.append(soma)


for soma_coluna in range(0,len(matriz)):
    cont = 0
    soma_colum = 0
    while cont!=5:
        soma_colum += matriz[cont][soma_coluna]
        cont+=1
    SC.append(soma_colum)    

print(SL,SC)