from time import sleep

saldo = 1000
limite = 0 
extrato = []
numero_saques = 0


menu = '''
|====================|
|     MARQS BANK     |
| 1 = Depositar      |
| 2 = Sacar          |
| 3 = Extrato        |
| 4 = Sair           |
|====================|
'''

while True:  # Loop principal
    #Exibir o menu principal
    print(menu)

    opcao = int(input("Informe a opção que deseja utilizar: "))
    sleep(1)
    #Opção de deposito
    if opcao == 1:
        deposito = float(input("Informe o valor que deseja depositar: "))
        if deposito <= 0:
            print("Operação não efetuada!\nÉ necessário realizar um depósito acima de R$0,00.")
            sleep(1)
        else:
            saldo += deposito
            print(f"O depósito de R${deposito:.2f} foi realizado com sucesso!\nSeu saldo atual é R${saldo:.2f}")
            extrato.append(f"Depósito: R${deposito:.2f}")
            sleep(1)
    
    #Opção de Saque
    elif opcao == 2:
        saque = float(input("Informe o valor que deseja sacar: "))
        if saque <= 0:
            print("Operação não efetuada!\nÉ necessário realizar um saque acima de R$0,00.")
            sleep(1)
        elif numero_saques >= 3 or (limite + saque) > 1500:
            print("Você já atingiu seu limite de saque diário!")
            sleep(1)
        elif saldo < saque:
            print(f"Saldo Insuficiente!\nSeu saldo é de: R${saldo:.2f}")
            sleep(1)
        else:
            saldo -= saque
            limite += saque
            numero_saques += 1
            print(f"o saque de R${saque:.2f} foi realizado com sucesso!\nSeu saldo atual é R${saldo:.2f}")
            extrato.append(f"Saque: R${saque:.2f}")
            sleep(1)

    #Opção de Saque
    elif opcao == 3:
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        sleep(1)            

    #Opção de encerramento.
    elif opcao == 4:
        print("Encerrando...")
        break

    else:
        print("Opção Inválida!")
        sleep(1)
