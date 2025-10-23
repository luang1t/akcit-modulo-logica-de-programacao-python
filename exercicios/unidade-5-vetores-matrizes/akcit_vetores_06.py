from random import randint
matriz = []

numero_colunas = int(input("Digite o numero de colunas: "))
numero_linhas = int(input("Digite o numero de linhas: "))
for _ in range(numero_linhas):
    matriz.append(list())

for linha in range(0, numero_linhas):
    for coluna in range(0, numero_colunas):
        while True:
            numero = randint(0,26)
            if any(numero in sub_linha for sub_linha in matriz):
                continue
            else:
                matriz[linha].append(numero)
                break
                
for linha in range(0,numero_linhas):
    for coluna in range(0,numero_colunas):
        print(f"[{matriz[linha][coluna]:^5}]",end = '')
    print()
    
consulta = int(input("Insira um número para saber se ele está na matriz: "))

valor_encontrado = False
linha_valor_encontrado = 0 
coluna_valor_encontrado = 0 

atual_linha = 0
for linha in matriz:
    for coluna in range(len(linha)):
        if linha[coluna] == consulta:
            valor_encontrado = True
            linha_valor_encontrado = atual_linha
            coluna_valor_encontrado = coluna
            break
    if valor_encontrado:
        break    
    atual_linha+=1
           
            
if valor_encontrado == True:
    print(f"O número {consulta} foi encontrado na linha {linha_valor_encontrado+1} coluna {coluna_valor_encontrado+1}.\n{matriz[linha_valor_encontrado][coluna_valor_encontrado]}")
else:
    print(f"Valor {matriz[linha_valor_encontrado][coluna_valor_encontrado]} não encontrado.")