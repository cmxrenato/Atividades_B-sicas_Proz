

def calc_de_dois_numeros(num1,num2,operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    else:
        resultado = 0

    return resultado


num1 = 25
num2 = 5
operacao = 2


print("O resultado da operação é: {}".format(calc_de_dois_numeros(num1,num2,operacao)))

