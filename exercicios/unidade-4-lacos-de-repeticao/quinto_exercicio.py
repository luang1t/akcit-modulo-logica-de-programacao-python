#Construa um algoritmo que leia um conjunto de dados contendo altura e sexo (“M” para masculino e “F” para feminino) de 50 pessoas e, depois, calcule e escreva:
#a maior e a menor altura do grupo;
#a média de altura das mulheres;
#o número de homens e a diferença porcentual entre eles e as mulheres.

#print("CALCULO DA MAIOR E DA MENOR ALTURA DO GRUPO\nA MÉDIA DE ALTURA DAS MULHERES\nO NÚMERO DE HOMENS E A DIFERENÇA PORCENTUAL ENTRE ELES E AS MULHERES.")
maior_mulher = float('-inf')
maior_homem = float('-inf')
menor_homem = float('inf')
menor_mulher = float('inf')

mulheres_cadastradas = 0
homens_cadastrados = 0
soma_altura_homens = 0
soma_altura_mulheres = 0

for i in range(2):
    sexo = str(input("Cadastro de 50 homens e mulheres com médias\nCadastroDigite 'M' para mulher e 'H' para homem: "))
    sexo_upper = sexo.upper()

    if sexo_upper == 'M':
        altura_mulher = float(input("Digite sua altura. Ex: 1.75\nDigite aqui: "))
        mulheres_cadastradas += 1
        soma_altura_mulheres += altura_mulher
        if (maior_mulher < altura_mulher):
            maior_mulher = altura_mulher
        else:
            maior_mulher = maior_mulher

        if (menor_mulher > altura_mulher):
            menor_mulher = altura_mulher
        else:
            menor_mulher = menor_mulher  

    elif sexo_upper =='H':
        altura_homem = float(input("Digite sua altura. Ex: 1.75\nDigite aqui: "))
        homens_cadastrados += 1
        soma_altura_homens += altura_homem
         
        if (maior_homem < altura_homem):
            maior_homem = altura_homem
        else:
            maior_homem = maior_homem
        if (menor_homem > altura_homem):
            menor_homem = altura_homem
        else:
            menor_homem = menor_homem 

total_pessoas = homens_cadastrados+mulheres_cadastradas
  

if(maior_homem>maior_mulher):
   print(f"O maior do grupo é um homem com {maior_homem}m")
else:
    print(f"O maior do grupo é uma mulher com {maior_mulher}m")   


if(menor_homem<menor_mulher):
    print(f"O menor do grupo é um homem com {menor_homem}m")
else:
    print(f"O menor do grupo é uma mulher com {menor_mulher}m") 


media_altura_mulheres_cadastradas = soma_altura_mulheres/mulheres_cadastradas
print(f"Média altura das mulheres cadastradas é de: {media_altura_mulheres_cadastradas}m")

media_altura_homens_cadastrados = soma_altura_homens/homens_cadastrados
print(f"Média altura dos homens cadastradas é de: {media_altura_homens_cadastrados}m")
print(f"Homens cadastrados: {homens_cadastrados}")

comparacao_homen = (homens_cadastrados/total_pessoas)*100
print(f"o numero de homens cadastrados equivale há {comparacao_homen: .2f}%")

comparacao_mulher = (mulheres_cadastradas/total_pessoas)*100
print(f"o numero de mulheres cadastrados equivale há {comparacao_mulher: .2f}%")


