

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

operacao = -1
while operacao != 0:

    print("*******************************************************************************")
    print("Utilize os números das opções para fazer as respectivas operações:  ")
    print("1 - Somar; \n"
          "2 - Subtrair;\n"
          "3 - Multiplicar;\n"
          "4 - Dividir;\n"
          "0 - Sair\n")
    operacao = int(input("Digite o número da operação escolhida: "))
    if operacao == 0:
        print("Você saiu!")
        break
    elif (operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4 ):
        print("Essa opção não existe!")
    else:
        num1 = int(input("Digíte o primeiro número: "))
        num2 = int(input("Digíte o segundo número: "))

        print("O resultado da operação é: {}".format(calc_de_dois_numeros(num1,num2,operacao)))


















