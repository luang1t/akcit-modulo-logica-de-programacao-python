from random import randint

notas = []

acima = 0
abaixo = 0
iguais = 0

for nota in range(50):
    nota = randint(1,10)
    notas.append(nota)


media = sum(notas)/len(notas)
media_arredondada = round(media)

for nota in notas:
    if nota > media_arredondada:
        acima+=1
    elif nota < media_arredondada:
        abaixo+=1
    elif nota == media_arredondada:
        iguais+=1

print(f"Notas dos alunos:\n{notas}")
print(f"MÉDIA Normal: {media}")
print(f"MÉDIA: {media_arredondada}")
print(f"Pessoa acima da média: {acima} alunos")                
print(f"Pessoa abaixo da média: {abaixo} alunos")
print(f"Pessoa iguais à média: {iguais} alunos")                
