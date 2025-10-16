letras = []
cont_letra = 0

while cont_letra != 10:
    letra = input("Digite uma letra do alfabeto: ").strip().lower()[0]
    if letra not in letras:
        letras.append(letra)
        cont_letra += 1
    else:
        print("Você digitou uma letra que ja tem no bd, tente novamente!")

print(letras)

while True:
    encontra = input("Digite uma letra para saber se tem no vetor letras: ").strip().lower()[0]
    if encontra in letras:
        print(f"A letra {encontra} se encontra na posicação {letras.index(encontra)} do vetor letras.")
        break
    else:
        print("Letra não encontrada.")    