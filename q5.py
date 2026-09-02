while True:
    try:
        saldo = float(input("Digite seu saldo: "))
        saque = float(input("Digite o valor do saque: "))

        if saque <= 0:
            print("\nErro: o valor do saque deve ser maior que zero!\n")
            continue

        if saque > saldo:
            print("\nSaldo insuficiente!")
            break
        else:
            saldo_restante = saldo - saque
            print("\nSaque realizado com sucesso!")
            
            
            if saldo_restante.is_integer():
                print(f"Saldo restante: {int(saldo_restante)}")
            else:
                print(f"Saldo restante: {saldo_restante:.2f}")
            break

    except ValueError:
        print("\nErro: digite apenas valores numéricos!\n")