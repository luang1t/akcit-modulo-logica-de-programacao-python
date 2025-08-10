#Para participar da "Categoria Ouro" do 1º Campeonato Mundial de Bolinha de Gude o jogador deve pesar entre 70 kg (inclusive) e 80 kg (inclusive) e medir de 1,75 m (inclusive) a 1,90 m (inclusive). Construa um algoritmo que leia a altura e o peso de um jogador e determine se o jogador está apto a participar do campeonato, mostrando uma das seguintes mensagens conforme cada situação:
#"Recusado por peso": se somente o peso do jogador for inválido;
#"Recusado por altura": se somente a altura do jogador for inválida;
#"Recusado por peso e altura": se a altura e o peso do jogador forem inválidos;
#"Aceito": se a altura e o peso do jogador estiverem dentro da faixa especificada.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

if ((altura>=1.75 and altura<=1.90) and (peso>=70 and peso<=80)):
    print("Aceito!")
elif (altura>=1.75 and altura<=1.90) and ((peso<70)or(peso>80)):
    print("Recusado, seu peso não é compativel!")
elif(((altura<1.75)or(altura>1.90))and(peso>=70 and peso<=80)):
    print("Recusado, sua altura não é compativel!")    
else:
    print("Rescusado, todos os dados não são compativeis")    
