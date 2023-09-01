import textwrap

saldo = 0 
limite = 500
extrato = []
usuarios = []
contas = []
saques_diarios = 0

LIMITE_SAQUES = 3
AGENCIA = '001'

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito:\tR$ {valor:.2f}\n")
            print(f"\n=== Operação realizada com sucesso! Você depositou R$ {valor:.2f}. ===\n")

        else:
            print("\n### Operação falhou! Insira um valor válido para prosseguir. ###")
        
        return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, saques_diarios, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = saques_diarios >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")

    elif excedeu_limite:
        print("\n### Operação falhou! O valor do sque excede o limite. ###")
        
    elif excedeu_saques:
        print("\n### Operação falhou! Número máximo de saques excedido. ###")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:\tR$ {valor:.2f}\n")
        saques_diarios += 1

        print(f"=== Saque de R$ {valor:.2f} realizado com sucesso. ===")

    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

def consultar_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    if not extrato:
        print("Não foram realizadas movimentações.")

    else:
        for movimentacao in extrato:
            print(movimentacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")  

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    #verificando se o usuário já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == 'cpf':
            print("\n ### CPF já cadastrado. Não é possível cadastrar o usuário novamente. ###")
            return

    #Cria um dicionário com os dados do usuário
    usuario = {
        "CPF": cpf, 
        "nome": nome, 
        "data de nascimento": data_nascimento, 
        "endereco": endereco
        }
    
    # Adiciona o usuário à lista de usuários
    usuarios.append(usuario)

    print("\n ===== Usuário cadastrado com sucesso! ======")

def cadastrar_conta(cpf_usuario):
    #verifica se o usuário tá com cpf cadastrado
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("\n### Usuário não foi localizado. Não é possível cadastrar a conta. ###")
        print("\n### Por favor, faça primeiro seu cadastro como cliente antes de realizar a abertura da conta. ###")
    
    #gera e mantém o número da conta sequencial
    num_conta = len(contas) + 1

    #criação do dicionário com os dados da conta corrente
    conta = {
        "agencia": "001",
        "num_conta": num_conta,
        "usuario": usuario_encontrado,
        "status": status
    }

    contas.append(conta)

    print("\n===== Conta cadastrada com sucesso! =====")
    print("\nVocê já pode realizar operações na sua conta bancária.")

def listar_usuarios():
    if not usuarios:
        print("\nNão há usuários cadastrados.")
    else:
        print("Usuários: ")
        for usuario in usuarios:
            print(f"CPF: {usuario['cpf']}, Nome: {usuario['nome']}")
    
def listar_contas():
    if not contas:
        print("\nNão há contas cadastrada para esse usuário.")

    else:
        print("Contas correntes:")
        for conta in contas:
            num_conta = conta["num_conta"]
            agencia = conta["agencia"]
            usuario = conta["usuario"]
            status = conta["status"]
            print(f"Conta: {agencia} - {num_conta} (CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Status da Conta: {conta['status']})")

def desativar_conta():
    listar_contas()

    cpf = int(input("Informe o CPF do usuário titular da conta"))
    listar_contas['cpf']
    selecionar_conta = int(input("Informe o número da conta a ser desativada: "))

    for conta in contas:
        num_conta = conta["num_conta"]
        agencia = conta["agencia"]
        usuario = conta["usuario"]
        status = conta["status"]
        print(f"A conta selecionada é: \nConta: {agencia} - {num_conta} (CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Status da Conta: {conta['status']})")
        escolha_desativar = input("\n Você deseja mesmo desativar essa conta? Y/N")

        if escolha_desativar == "Y":
            selecionar_conta = conta.get("status")
            conta["status"] = "Desativada"
            print("\nConta desativada.")

        else:
            print("\nVocê pode escolher outra opção: ")

def reativar_conta():
    for conta in contas:
        num_conta = conta["num_conta"]
        agencia = conta["agencia"]
        usuario = conta["usuario"]
        status = conta["status"]
        print(f"A conta selecionada é: \nConta: {agencia} - {num_conta} (CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Status da Conta: {conta['status']})")
        escolha_reativar = input("\n Você deseja reativar essa conta? Y/N")

        if escolha_reativar == "Y":
            selecionar_conta = conta.get("status")
            conta["status"] = "Desativada"
            print("\nConta reativada. Você já pode utilizá-la para operações bancárias.")

        else:
            print("\nVocê pode escolher outra opção: ")

def exibir_menu():
    menu = """
    =============== MENU ===============
    Você já é cliente?
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tDesativar conta
    
    Ainda não é cliente?
    [5]\tCadastrar Cliente
    [6]\tBuscar cliente
    [7]\tCadastrar nova conta
    [8]\tBuscar conta
    [9]\tReativar conta
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
     
    while True:
        opcao = exibir_menu()
        global saldo, extrato, saques_diarios

        # Opção 1: Depósito
        if opcao == "1":
            print("\n=============== DEPÓSITO ===============")
            valor = float(input("Informe o valor a ser depositado:"))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        # Opção 2: Saque
        elif opcao == "2":
            print("\n=============== SAQUE ===============")
            valor = float(input("Informe o valor a ser sacado: "))
            saldo, extrato, saques_diarios = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                saques_diarios=saques_diarios
                )

        # Opção 3: Consultar extrato
        elif opcao == "3":
            consultar_extrato(saldo, extrato=extrato)

        # Opção 4: Desativar conta
        elif opcao == "4":
            desativar_conta()
        
        # Opção 5: Cadastrar usuário
        elif opcao == "5":
            cpf = int(input("Informe o CPF (somente números): "))
            nome = input("Informe nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)

        # Opção 6: Listar Usuários
        elif opcao == "6":
            # cpf_usuario = int(input("\n Para localizar o usuário, digite o CPF do titular da conta: "))
            listar_usuarios()

        # Opção 7: Cadastrar conta
        elif opcao == "7":
            cpf_usuario = int(input("\n Digite o CPF do usuário titular da conta: "))
            cadastrar_conta(cpf_usuario)

        # Opção 8: Listar contas
        elif opcao == "8":
           # cpf = int(input("Para buscarmos todas as contas já abertas para o titular, informe o CPF do usuário titular da conta: "))
            listar_contas()

        # Opção 9: Reativar conta
        elif opcao == "9":
            cpf = int(input("Para buscarmos todas as contas já abertas para o titular, informe o CPF do usuário titular da conta: "))
            listar_contas['registro_usuario']
            agencia = '001'
            num_conta = int(input("Informe o número da conta a ser reativada: "))
            reativar_conta()

        # Opção 0: Sair
        elif opcao == "0":
            print("Obrigado por utilizar nossos sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()