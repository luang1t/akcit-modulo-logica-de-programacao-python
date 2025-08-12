#Elabore um algoritmo que determine o valor de S, em que:
#S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + … - 10/100.
soma_total = 0
soma_pares = 0
soma_impares = 0
divisao = 0
for i in range (1,11):
    a = i
    b = i**2 

    if(a % 2 != 0):
        divisao = a/b
        resultado_impar = divisao
        soma_impares_positivos += resultado_impar
        print(f"{a}/{b}")
    else:
        divisao = a/b
        resultado_par = divisao * - 1
        soma_pares_negativos += resultado_par
        print(f"{a}/{b}")

soma_total = (soma_pares + soma_impares)       
print(f"{soma_total}")        