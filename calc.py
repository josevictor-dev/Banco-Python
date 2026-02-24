def equacoes(operacao):
    def somar(a,b):
        return a+b
    def multiplicar(a,b):
        return a*b 
    def subtrair(a,b):
        return a-b
    
    if operacao == '+':
        return somar
    if operacao == '*':
        return multiplicar
    else:
        return subtrair
    


resultado = equacoes('*')(1, 3)

print(resultado)