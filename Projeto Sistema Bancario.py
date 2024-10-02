menu = '''

  Selecione uma opção:

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair


'''

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
           saldo += valor
           extrato += f'Deposito no valor de: R$ {valor:.2f}\n'
           print("Deposito realizado com sucesso!")

        else:
           print("Operação cancelada, valor inserido é invalido!")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))
        
        if valor > 0:
         
         if saldo >= valor and numero_saques < LIMITE_SAQUES and valor <= limite:
            print("Saque Realizado")
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque no valor de: R$ {valor:.2f}\n'
         
         elif saldo < valor:
            print("Não foi possivel realizar o saque, saldo insuficiente!")
         
         elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possivel realizar o saque, limite diario de saques alcançado!")
         
         elif valor > limite:
            print("Não foi possivel realizar o saque, limite inferior ao valor solicitado!")
        
        else:
           print("Operação cancelada, valor inserido é invalido!")


    elif opcao == "3":
        print("\n================EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$: {saldo:.2f}')
        print("======================================") 

    elif opcao == "0":
        print("Obrigado por usar nosso banco!")
        break

    else:
        print("Opção invalida, por favor selecione novamente a operação desejada.")

   


