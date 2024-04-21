
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
        
        while saque<0:
            print("Não é permitido valor negativo")
            saque=float(input("Entre com valor a ser sacado: "))
        else:
            if numero_saques <= LIMITE_SAQUES or saque <= limite:
                if saque<=saldo:
                    saldo-=saque
                    numero_saques+=1
                    extrato+= """
        Saque ---------------R${:.2f} """.format(saque)
                else:
                    print("Não será possível sacar o dinheiro por falta de saldo")
            else:
                print("Limite diário estourado")

        
        print("*******************************************")
        saque=0

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