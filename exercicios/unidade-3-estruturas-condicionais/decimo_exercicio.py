while True:
        try:
            print("--- Menu Aplicação ---")
            print("1 - Imposto a ser pago e salário final.")
            print("2 - Novo salário com aumento.")
            print("3 - Classificação")
            seletor = int(input("Digite a opção desejada: "))
            if (seletor == 1) or (seletor == 2) or (seletor == 3):
                if seletor == 1:
                        while True:
                            try:
                                print("--- IMPOSTO A SER PAGO ---")
                                salario_funcionario = float(input("Digite o seu salário: "))
                                if (salario_funcionario > 0):
                                    break
                                else:
                                    print("Digite o valor maiores que 0!")
                            except ValueError:
                                print("Digite um valor real.")

                        if (salario_funcionario < 1100): 
                            cinto_porcento = salario_funcionario * 0.05  
                            novo_salario = salario_funcionario - cinto_porcento
                            print(f"Salário normal | R$:{salario_funcionario:.2f}") 
                            print(f"Decrescimo de 5% | R$:{cinto_porcento:.2f}") 
                            print(f"Salário com decrescimo de 5% | R$:{novo_salario:.2f}") 

                        elif (salario_funcionario >= 1100) and (salario_funcionario <= 3000):
                            dez_porcento = salario_funcionario * 0.1
                            novo_salario = salario_funcionario - dez_porcento
                            print(f"Salário normal | R$:{salario_funcionario:.2f}") 
                            print(f"Decrescimo de 10% | R$:{dez_porcento:.2f}") 
                            print(f"Salário com decrescimo de 10% | R$:{novo_salario:.2f}")

                        else:
                            quinze_porcento = salario_funcionario * 0.15
                            novo_salario = salario_funcionario - quinze_porcento
                            print(f"Salário normal | R$:{salario_funcionario:.2f}") 
                            print(f"Decrescimo de 15% | R$:{quinze_porcento:.2f}") 
                            print(f"Salário com decrescimo de 15% | R$:{novo_salario:.2f}")

                elif seletor == 2:
                    while True:
                        try:
                            print("--- NOVO SALARIO COM AUMENTO ---")
                            salario_funcionario = float(input("Digite o seu salário: "))
                            if salario_funcionario > 0:
                                break
                            else:
                                print("Digite um valor maior que 0!")
                        except ValueError:
                            print("Digite um valor real positivo!")
                    if (salario_funcionario < 1500):
                        novo_salario = salario_funcionario + 100
                        print(f"Salário normal | R$:{salario_funcionario:.2f}")
                        print(f"Acrescimo | R$:100.00")
                        print(f"Salário com acrescimo | R$:{novo_salario:.2f}")

                    elif (salario_funcionario >= 1500) and (salario_funcionario < 2000):
                        novo_salario = salario_funcionario + 250
                        print(f"Salário normal | R$:{salario_funcionario:.2f}")
                        print(f"Acrescimo de R$:250.00")
                        print(f"Salário com acrescimo | R$:{novo_salario:.2f}")
                    elif (salario_funcionario >= 2000) and (salario_funcionario <= 3000):
                        novo_salario = salario_funcionario + 300
                        print(f"Salário normal | R$:{salario_funcionario:.2f}")
                        print(f"Acrescimo | R$:300.00")
                        print(f"Salário com acrescimo | R$:{novo_salario:.2f}")
                    else:
                        novo_salario = salario_funcionario + 450
                        print(f"Salário normal | R$:{salario_funcionario:.2f}")
                        print(f"Acrescimo | R$:450.00")
                        print(f"Salário com acrescimo | R$:{novo_salario:.2f}")
                elif seletor == 3:
                    while True:
                        try:
                            print("--- CLASSIFICAÇÃO DE SALÁRIO ---")
                            salario_funcionario = float(input("Digite o seu salário: "))  
                            if salario_funcionario > 0:
                                break
                            else:
                                print("Digite um número maior que 0!")
                        except ValueError:
                            print("Digite apenas números maiores que 0!")
                    if salario_funcionario<1500:
                        print(f"MAL REMUNERADO | R$:{salario_funcionario}")   
                    else:
                        print(f"BEM REMUNERADO | R$:{salario_funcionario}")
                    
                break
            else:
                print("Digite 1,2 ou 3.") 
        except ValueError:
            print("Digite 1, 2 ou 3.")
