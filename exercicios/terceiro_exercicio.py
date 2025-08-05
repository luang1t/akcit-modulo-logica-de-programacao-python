# Escreva um algoritmo que determine o consumo médio de combustível de um automóvel após recebidas a distância total percorrida e a quantidade de combustível gasto.

distancia_total = float(input("Digite a distancia total percorrida: "))
combustivel_gasto = float(input("Digite a quantidade gasta de combustivel na viagem: "))
consumo_medio = distancia_total/combustivel_gasto
print(f"Você percorreu {distancia_total}Km e gastou um total de {combustivel_gasto}L com um consumo médio de {consumo_medio}Km/Litro")
