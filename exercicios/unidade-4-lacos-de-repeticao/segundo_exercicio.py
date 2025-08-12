#Elabore um algoritmo que determine o valor de S, em que:
#S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + … - 10/100.
soma_total = 0
soma_pares_negativos = 0
soma_impares_positivos = 0
divisao = 0
for i in range (1,11):
    a = i
    b = i**2 

    if(a % 2 != 0):
        divisao = a/b
        soma_impares_positivos += divisao
        print(f"{a}/{b}")
    else:
        divisao = a/b        
        soma_pares_negativos += (divisao*-1)
        print(f"{a}/{b}")

soma_total = (soma_pares_negativos + soma_impares_positivos)       
print(f"{soma_total}")        