def dados():
    nome = str(input("Digite seu nome:\n"))
    ano_nascimento = int(input("Digite o ano de nascimento:\n"))
    ano_atual = 2024
    idade = ano_atual - ano_nascimento
    return nome,ano_nascimento,ano_atual,idade

if __name__ == "__main__":
    nome,ano_nascimento,ano_atual,idade = dados()
    print(f"Olá {nome}!")
    print(f"Com os dados fornecidos identificamos que seu nome é {nome} nasceu no ano de {ano_nascimento} e tem {idade} anos de idade atualmente em {ano_atual}.")