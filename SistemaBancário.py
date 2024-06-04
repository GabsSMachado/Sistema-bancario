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
        valor = float(input('Informe o valor do seu depósito'))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de : R$ {valor:.2f}\n"

        else: ("Oops, operação falhou! O valor informado é inválido!")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque"))

        excedeuSaldo = valor > saldo

        excedeuLimite = valor > limite

        excedeuSaques = numero_saques >= LIMITE_SAQUES

        if excedeuSaldo:
            print("Oops, operação falhou! Você não tem saldo suficiente para esta transação!")
        
        elif excedeuLimite:
            print("Oops, operação falhou! Você excedeu o liite permitido para esta transação!")
        
        elif excedeuSaques:
            print("Oops, operação falhou! Você excedeu a quantidade de saques diários permitido!")

        elif valor > 0 and valor <= 500:
            saldo -= valor
            extrato += f"Saque efetuado de : R$ {valor:.2f}\n"
            numero_saques += 1

        else: ("Oops, operação falho! O valor informado é inválido")

    elif opcao == "e":
            print("\n ============== EXTRATO ===============")
            print("Não foram efetuadas transações" if not extrato else extrato )
            print(f"\n O seu saldo é : R$ {saldo:.2f}")
            print("\n======================================")
        
    elif opcao == "q":
            break
    
    else:
        print("Operação inválida!")