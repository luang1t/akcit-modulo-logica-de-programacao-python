#No planeta Alpha vive a criatura Blobs, que come precisamente 1/2 de seu suprimento de comida disponível todos os dias. Escreva um algoritmo que leia a capacidade inicial de suprimento de comida em quilos, e calcule quantos dias passarão antes que os Blobs comam todo esse suprimento até atingir 1 quilo ou menos.
suprimentos_totais = int(input("Digite a quantidade de suprimentos: "))
dias = 0

while  suprimentos_totais >= 1 :
    subtra = suprimentos_totais/2
    suprimentos_totais -= subtra
    dias += 1
print(f"{dias}")        