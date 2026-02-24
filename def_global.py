salario = 1500


def bonus(valor):
    global salario
    salario += valor
    return salario


print(bonus(1000))