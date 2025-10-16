from random import randint

mega_sena = []
numeros_acertos = []
numeros_player = []
numeros_hit = 0
cont_mega = 0
cont_jogador = 0


while cont_mega != 6:
    numero = randint(1,61)
    if numero not in mega_sena:
        mega_sena.append(numero)
        cont_mega+=1

print(mega_sena)        

while cont_jogador != 6:
    numero = int(input(f"Digite {cont_jogador+1}º número: "))
    if numero not in numeros_player:    
        numeros_player.append(numero)
        cont_jogador+=1
        if numero in mega_sena:
            numeros_acertos.append(numero)
            numeros_hit+=1
    else:
        print("Esse numero ja foi cadastrado, tente novamente com outro numero.")    


print(f"Números sorteados:\n{mega_sena}")
print(f"Números do jogador:\n{numeros_player}")
     
if numeros_hit == 0:
    print(f"O jogador não acertou nada :,(")
else:
    print(f"O jogador acertou um total de {numeros_hit} números.\nEsse são os números hitados\n{numeros_acertos}")  