#Um mercado está vendendo frutas de acordo com a seguinte tabela de preços:

#Morango até 5KG = R$5:00 | Acima de 5KG R$4:00
#Maça  até   5KG = R$3:00 | Acima de 5KG R$2:00

#Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$35,00, receberá ainda um desconto de 20% sobre esse total. Escreva um algoritmo que receba a quantidade (em kg) de morangos e a quantidade (em kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input("Digite a quantidade em quilos(Kg) de morangos que você comprou: "))
maca = float(input("Digite a quantidade em quilos(Kg) de maçãs que você comprou: "))

if maca < 0:
    maca = 0
else:
    maca = maca
if morango < 0:
    morango = 0
else:
    morango = morango 

if (maca <= 5):
    final_maca = (maca*3)
elif (maca > 5):
    final_maca = (maca*2)
else:
    print("Maça menor que zero.") 
    
if (morango <= 5):
    final_morango = (morango*5)
elif (morango > 5):
    final_morango = (morango*4)
else:
    print("Morango menor que zero.")   

preco_final = final_maca+final_morango
quilos_totais = morango+maca


if(quilos_totais > 8 or preco_final > 35):

    vinte_porcento = preco_final * 0.2
    preco_desconto = preco_final - vinte_porcento
    print(f"Extrato:")
    print(f"{maca}x - Maças R$:{final_maca:.2f}")
    print(f"{morango}x - Morangos R$:{final_morango:.2f}")
    print(f"Parabéns!\nDesconto de 20%\n R$:{preco_final}\n-R$:{vinte_porcento}\nDeve pagar R$:{preco_desconto:.2f}")
else:
    print(f"Extrato:")
    print(f"{maca}x - Maças R$:{final_maca:.2f}")
    print(f"{morango}x - Morangos R$:{final_morango:.2f}")
    print(f"Deve pagar R$:{preco_final:.2f}.")    

