from random import randint
matriz = []

numero_linhas = int(input("Digite o numero de linhas:"))
numero_colunas = int(input("Digite o numero de colunas:"))

for _ in range(0,numero_linhas):
    matriz.append(list())

for linha in range(0,numero_linhas):
    for coluna in range(0,numero_colunas):
        while True:
            numero = randint(0,26)
            if any(numero in sub_linha for sub_linha in matriz):
                continue
            else:
                matriz[linha].append(numero)
                break
for prnt_linha in range(0,numero_linhas):
    for prnt_coluna in range(0,numero_colunas):
        print(f"[{matriz[prnt_linha][prnt_coluna]:^5}]", end = '')
    print()

consulta = int(input("Digite um número para saber se existe ou não na matriz: "))
numero_encontrado = False

for cslt_linha in range(0,numero_linhas):
    for cslt_coluna in range(0,numero_colunas):
        if matriz[cslt_linha][cslt_coluna] == consulta:
            print(f"{consulta} encontrado na linha {cslt_linha} coluna {cslt_coluna}.")
            numero_encontrado = True
            break

if numero_encontrado == False:
    print(f"Numero {consulta} não encontrado.")