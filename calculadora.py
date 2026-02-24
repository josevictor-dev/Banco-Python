def soma(a,b):
    return a+b
def multiplicacao(a,b):
    return a*b
def resultado(a,b,equacao):
    resolucao = equacao(a,b)
    print(f'O resultado da equção foi {resolucao}')



while True:
    
    
    
    try:
        valor1 = int(input('Valor 1'))
        operador = input('Digite o op')
        valor2 = int(input('Valor 2'))
    except:
        print('o valor precisa ser inteiro')
        continue
        

    if operador == '+':
        print(f'O valor de {valor1} + {valor2} é igual a', resultado(valor1, valor2, soma))
    if operador == '*':
        print(f'O valor de {valor1} + {valor2} é igual a', resultado(valor1, valor2, multiplicacao))