# Uma agência de publicidade quer prestar serviços somente para as maiores companhias (em números de funcionários ) em cada uma das classificações: grande, média, pequena e microempresa. Para tal, deve ser fornecido pelo(a) usuário(a) um conjunto de dados com o código, o número de funcionários e o porte da empresa. Construa um algoritmo que liste o código da empresa com maiores recursos humanos dentro de cada categoria. Utilize como finalizador o código de empresa igual a 0.


codigo_empresa = 1
codigo_maior_microempresa = 0
codigo_maior_pequena_empresa = 0
codigo_maior_media_empresa = 0
codigo_maior_grande_empresa = 0 
maior_microempresa = 0
maior_pequenaempresa = 0
maior_mediaempresa = 0
maior_grandeempresa = 0

print("Vamos ver quais empresas estão mais qualificadas para investirmos baseados no porte de empresa: ")

while codigo_empresa !=0 :        
        codigo_empresa = int(input("Digite o código da empresa ou '0' para finalizar o programa: "))
        if codigo_empresa == 0:
            break
        numero_funcionario = int(input("Digite o numero de funcionários: "))
        if (numero_funcionario <= 9):
            nova_microempresa = numero_funcionario
            if(nova_microempresa > maior_microempresa):
                maior_microempresa = nova_microempresa
                codigo_maior_microempresa = codigo_empresa                

        elif (numero_funcionario >= 10 and numero_funcionario <= 49):
            nova_pequena_empresa = numero_funcionario
            if(nova_pequena_empresa > maior_pequenaempresa):
                 maior_pequenaempresa = nova_pequena_empresa
                 codigo_maior_pequena_empresa = codigo_empresa

        elif (numero_funcionario >=50 and numero_funcionario <= 99):
             nova_media_empresa = numero_funcionario
             if(nova_media_empresa > maior_mediaempresa):
                maior_mediaempresa = nova_media_empresa
                codigo_maior_media_empresa = codigo_empresa
                
        else:
             nova_grande_empresa = numero_funcionario
             if(nova_grande_empresa > maior_grandeempresa):
                maior_grandeempresa = nova_grande_empresa
                codigo_maior_grande_empresa = codigo_empresa
                

print("---------------------------------------")
print("A maior microempresa: ")
print(f"Código: {codigo_maior_microempresa}")
print(f"Funcionários: {maior_microempresa}")
print("---------------------------------------")
print("A maior pequena empresa: ")
print(f"Código: {codigo_maior_pequena_empresa}")
print(f"Funcionários: {maior_pequenaempresa}")
print("---------------------------------------")
print("A mior média empresa: ")
print(f"Código: {codigo_maior_media_empresa}")
print(f"Funcionários: {maior_mediaempresa}")
print("---------------------------------------")
print("A maior grande empresa: ")
print(f"Código: {codigo_maior_grande_empresa}")
print(f"Funcionários: {maior_grandeempresa}")
print("---------------------------------------")

                  
                          
                       
    