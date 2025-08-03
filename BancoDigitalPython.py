def exibir_menu():
    return """
    ================= MENU =================

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =======================================

    => """


def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! Valor inválido.")
    except ValueError:
        print("❌ Entrada inválida! Informe um número.")
    return saldo, extrato


def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("❌ Operação falhou! Valor inválido.")
        elif valor > saldo:
            print("❌ Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("❌ Operação falhou! Limite por saque excedido.")
        elif numero_saques >= limite_saques:
            print("❌ Operação falhou! Limite diário de saques atingido.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso!")

    except ValueError:
        print("❌ Entrada inválida! Informe um número.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================\n")


def main():
    saldo = 0.0
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(exibir_menu()).lower()

        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'q':
            print("🏦 Obrigado por usar nosso banco. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
