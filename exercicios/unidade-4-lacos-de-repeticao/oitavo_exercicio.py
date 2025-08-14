#Um pecuarista deseja obter o maior peso entre os animais de seu rebanho, mas não sabe a quantidade total de animais. Faça um algoritmo que receba os pesos de todos os animais utilizando um laço de repetição e, após a leitura do último, diga quantos animais o rebanho possui e qual o maior peso. Considere como condição finalizadora, para encerrar a leitura, o peso do animal sendo 0.
peso = 0
maior_animal = " "
mais_pesado = 0
animais_contagem = 0

while peso !=0 :
    animal = str(input("Quando quiser sair e ver resultado aperte '0'\nDigite o nome do animal:"))
    peso = float(input("Digite o peso: "))
    if mais_pesado<peso:
        mais_pesado=peso
        maior_animal = animal
    animais_contagem+=1
print(f"Animal mais pesado é o {maior_animal} com {mais_pesado}kg")        