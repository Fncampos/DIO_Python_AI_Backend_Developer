
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        print("*******************************************")
        deposito=float(input("Entre com valor a ser depositado: "))
        
        while deposito<0:
            print("Não é permitido valor negativo")
            deposito=float(input("Entre com valor a ser depositado: "))
        else:
            saldo+=deposito

        extrato+= """
        Depósito ------------R${:.2f} """.format(deposito)
        print("*******************************************")
        deposito=0
    
    elif opcao == "s":
        print("Saque")
        print("*******************************************")
        saque=float(input("Entre com valor a ser sacado: "))
        
        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        while saque<0:
            print("Não é permitido valor negativo")
            saque=float(input("Entre com valor a ser sacado: "))
        else:
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif saque > 0:
                saldo-=saque
                numero_saques+=1
                extrato+= """
        Saque ---------------R${:.2f} """.format(saque)
            
            else:
                print("Operação falhou! O valor informado é inválido")

        print("*******************************************")
       

    elif opcao == "e":
        print("Extrato")
        print("*******************************************")
        print(extrato)
        print("""
        SALDO ----------------R${:.2f} """.format(saldo))
        print("*******************************************")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")