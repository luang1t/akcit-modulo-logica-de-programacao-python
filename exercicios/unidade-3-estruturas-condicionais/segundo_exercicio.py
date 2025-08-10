#Escreva um algoritmo que verifique a validade de uma senha fornecida pelo(a) usuário(a). A senha válida é o número 1234. Caso a senha seja válida deve ser mostrada a mensagem “Acesso permitido”, caso contrário, se a senha for inválida, deve ser mostrada a mensagem “Acesso negado”.

senha_acesso = str(input("Digite a senha de acesso: "))

if(senha_acesso == "1234"):
    print("Acesso permitido!")
else:
    print("Acesso negado!")    