#Escreva um algoritmo que leia um valor X e um valor Z (se Z for menor que X deve ser lido um novo valor para Z). Em seguida conte e mostre quantos números inteiros devemos somar em sequência, a partir do X (inclusive), (X, X+1, X+2, X+3, ...) para que a soma ultrapasse o valor de Z o mínimo possível.

valor_x = int(input("Digite o valor de x: "))
valor_z = int(input("Digite o valor de z: "))
soma=0
i=0
atual=valor_x

while valor_x > valor_z:
    print("Digite o valor onde Z é maior que X: ")
    valor_z = int(input("Digite o valor de z: ")) 

while soma <= valor_z:
        soma+=atual
        i+=1
        atual+=1
        print(f"{valor_x}+{i-1}")