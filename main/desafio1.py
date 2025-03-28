menu = """
Selecione uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto irá depositar?"))


        if valor > 0:

            saldo += valor
            extrato += f'Depósito no valor de R$ {valor:.2f}.\n '


            print(f"Depósito realizado com sucesso. Seu novo saldo é R$ {saldo} Reais.")
        else:
            print(f"O valor depositado precisa ser positivo")
            continue


    elif opcao == "s":

        retirada = float(input(f"Quanto gostaria de sacar?"))
        # Iremos realizar as verificações e atribuir a variável

        excedeu_saldo = retirada > saldo

        excedeu_limite = retirada > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE


        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f'Você atingiu o limite diário')
        elif excedeu_saque:
            print(f'Você atingiu o limite de saques diários')

        elif retirada > 0:
            saldo -= retirada
            extrato += f'Saque R$ {retirada:.2f}.\n '
            numero_saque += 1

        else:
            print("O valor do Saque precisa ser positivo.")

    elif opcao == "e":
        print(f'=================EXTRATO==============\n')
        print(f'Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print(f'======================================')

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, tente novamente.")
