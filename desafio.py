menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 500
listaextrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def sacar(valor):
    global saldo, listaextrato, numero_saques
    

    if valor > saldo:
        return f'O valor execedeu o limite do saldo {saldo}'
    if valor > limite:
        return f'O valor excedeu o limite de {limite} por saque'
    if numero_saques >= LIMITE_SAQUES:
        return f'Você excedeu o limite de 3 saques'
    
    saldo -= valor
    numero_saques += 1
    listaextrato.append(f'- {valor}\nSaldo: {saldo}')
    



def deposito(valor):
    global saldo, listaextrato
    saldo += valor
    listaextrato.append(f'+ {valor}\nSaldo: {saldo}')



def extrato(listagem):
     print("\n================ EXTRATO ================")
     for i, valores in enumerate(listagem):
        print(f'{i}) ', valores)
        
        








while True:
    print(menu)

    opção = input('Qual opção deseja escolher: ')

    if opção == 's':
        saque = float(input('Qual valor de saque'))
        print(sacar(saque))

    if opção == 'd':
        saque = float(input('Qual valor de depósito'))
        print(deposito(saque))

    if opção == 'e':
        extrato(listaextrato)

    if opção == 'q':
        print('Saindo...')
        break





