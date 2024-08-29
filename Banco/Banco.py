from time import sleep

def menu():
    menu_texto = '''
|=====================|
|     MARQS BANK      |
| 1 = Depositar       |
| 2 = Sacar           |
| 3 = Extrato         |
| 4 = Novo Usuário    |
| 5 = Nova Conta      |
| 6 = Listar Contas   |
| 7 = Sair            |
|=====================|
'''
    print(menu_texto)
    return int(input("Informe a opção desejada: "))  # Convertendo para inteiro

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação não efetuada!\nÉ necessário realizar um depósito acima de R$0,00.")
        sleep(1)
    else:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")  # Adicionando à lista
        print(f"O depósito de R${valor:.2f} foi realizado com sucesso!\nSeu saldo atual é R${saldo:.2f}")
        sleep(1)
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"Operação negada! Você não tem saldo suficiente.\nSaldo atual: R${saldo:.2f}")

    elif excedeu_limite:
        print(f"Operação negada! O valor do saque excede o limite disponibilizado.\nLimite atual: R${limite:.2f}")

    elif excedeu_saques:
        print(f"Operação negada! O número máximo de saques foi excedido.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")  # Adicionando à lista
        print("Saque realizado com sucesso!")
        sleep(1)

    else:
        print("Operação negada! O valor informado não é válido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("==========================================")
    print("                EXTRATO                   ")
    print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com êxito!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("CPF não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            Conta: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("="*100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"            
    saldo = 0
    limite = 500 
    extrato = []  # Agora é uma lista de strings
    numero_saques = 0
    usuarios = []
    contas = []

    while True:  # Loop principal
        # Exibir o menu principal
        opcao = menu()
        sleep(1)

        # Opção de depósito
        if opcao == 1:
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            sleep(1)

        # Opção de saque
        elif opcao == 2:
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            numero_saques += 1  # Incrementando o número de saques
            sleep(1)
        # Opção de extrato
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)     
            sleep(1)     

        # Opção para criar novo usuário
        elif opcao == 4:
            criar_usuario(usuarios)
            sleep(1)
        # Opção para criar nova conta
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            sleep(1)

        # Opção para listar as contas criadas
        elif opcao == 6:
            listar_contas(contas)
            sleep(1)

        # Opção de encerramento
        elif opcao == 7:
            print("Encerrando...")
            sleep(1)
            break

        else:
            print("Opção Inválida!")
            sleep(1)

main()