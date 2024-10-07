
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3



def mostrar_menu():
    global saldo, limite, numero_saques, limite_saques, extrato
    print("")
    print("-----------------------------------------")   
    print("-----Seja bem-vindo ao banco norter------")
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[4] Sair")
    opcao = input("Digite sua escolha: ")
    print("-----------------------------------------")


    if opcao == "1":
        #deposito
        print("-------Depósito-------")
        valor = float(input("Digite o valor do seu depósito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            print("----------------------")
        else:
            print("esse valor é invalido tente novamente!")
            print("------------------")
    elif opcao =="2":
        #saque
        print("--------Saque----------")
        valor = float(input("Digite o valor do seu saque:"))

        excedeu_saldo =  valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Saque não foi realizado pois ultrapassa o valor do saldo atual!")
            print("-----------------------")
        elif excedeu_limite:
            print("Saque não foi realizado pois excede o limite do valor de saque")
            print("-----------------------")
        elif excedeu_saques:
            print("Saque não foi realizado pois excede o limite de saques diarios")    
            print("-----------------------")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            print("-----------------------")
        else:
            print("não foi possivel realizar o saque tente novamente")
            print("-----------------------")

    elif opcao =="3":
        #extrato
        print("----------------------")
        print("Não foram realizadas nenhuma transação" if not extrato else extrato)
        print(f"extrato atual: R$ {saldo:.2f}")    
        print("----------------------")
        
    elif opcao =="4":
        #sair
        print("Obrigado por utilizar o banco norter.  até logo!")
        exit()

    else:
        print("Essa opção não é valida")

while True:
    mostrar_menu()
    