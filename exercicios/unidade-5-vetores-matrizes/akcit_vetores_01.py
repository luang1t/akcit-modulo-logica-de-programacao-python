numeros = []
numeros_invertido = []

for numero in range(30):
    numeros.append(numero)
print(numeros)

for numero in range(len(numeros)):
    numeros_invertido.append(numeros[-(numero+1)])
    
    
print(numeros_invertido)    