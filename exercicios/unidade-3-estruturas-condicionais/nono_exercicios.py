while True:
    try:
        seletor = int(input("Digite 1 para onde crescente 2 para descresente e 3 para o maior no meio: "))
        if seletor == 1 or seletor == 2 or seletor == 3:
            if seletor == 1:
                while True:
                    try:
                        a = float(input("Digite o primeiro valor que será digitado como 'A': "))
                        b = float(input("Digite o primeiro valor que será digitado como 'B': "))
                        c= float(input("Digite o primeiro valor que será digitado como 'C': "))
                        if (a>b or b>a) and (a>c or c>a) and (b>c or c>b):
                            break
                        else:
                            print("Digite valores diferentes!")

                    except ValueError:
                        print("Digite numeros reais!")

                if a>b and b>c:
                    print(f"{c},{b},{a}")
                elif a>c and c>b:
                    print(f"{b},{c},{a}")    
                elif b>c and c>a:
                    print(f"{a},{c},{b}") 
                elif b>a and a>c:
                    print(f"{c},{a},{b}") 
                elif c>a and a>b:
                    print(f"{b},{a},{c}")
                elif c>b and b>a:
                    print(f"{a},{b},{c}")  

            elif seletor == 2:
                    while True:
                        try:
                            a = float(input("Digite o primeiro valor que será digitado como 'A': "))
                            b = float(input("Digite o primeiro valor que será digitado como 'B': "))
                            c= float(input("Digite o primeiro valor que será digitado como 'C': "))
                            if (a>b or b>a) and (a>c or c>a) and (b>c or c>b):
                                break
                            else:
                                print("Digite valores diferentes!")

                        except ValueError:
                            print("Digite numeros reais!")

                    if a>b and b>c:
                        print(f"{a},{b},{c}")
                    elif a>c and c>b:
                        print(f"{a},{c},{b}")    
                    elif b>c and c>a:
                        print(f"{b},{c},{a}") 
                    elif b>a and a>c:
                        print(f"{b},{a},{c}") 
                    elif c>a and a>b:
                        print(f"{c},{a},{b}")
                    else:
                        print(f"{c},{b},{a}")
            
                

            elif seletor == 3:
                    while True:
                        try:
                            a = float(input("Digite o primeiro valor que será digitado como 'A': "))
                            b = float(input("Digite o primeiro valor que será digitado como 'B': "))
                            c= float(input("Digite o primeiro valor que será digitado como 'C': "))
                            if (a>b or b>a) and (a>c or c>a) and (b>c or c>b):
                                break
                            else:
                                print("Digite valores diferentes!")

                        except ValueError:
                            print("Digite numeros reais!")

                    if a>b and b>c:
                        print(f"{b},{a},{c}")
                    elif a>c and c>b:
                        print(f"{c},{a},{b}")    
                    elif b>c and c>a:
                        print(f"{c},{b},{a}") 
                    elif b>a and a>c:
                        print(f"{a},{b},{c}") 
                    elif c>a and a>b:
                        print(f"{a},{c},{b}")
                    elif c>b and b>a:
                        print(f"{a},{c},{b}")
            break
        else:
            print("Digite 1, 2 ou 3 apenas!")
    except ValueError:
        print("Digite apenas 1, 2 ou 3!")         