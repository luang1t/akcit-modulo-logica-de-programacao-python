from random import randint

vetor = []

for numero in range(10):
    numero = randint(1,100)
    vetor.append(numero)

print(vetor)

for i in range(len(vetor)//2):
    troca = vetor[i]
    vetor[i] = vetor[-(i+1)]
    vetor[-(i+1)] = troca


print(vetor)    