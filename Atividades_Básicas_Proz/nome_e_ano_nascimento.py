
anoNasc = True
nome = input("Por favor, informe seu nome completo: ")

while anoNasc:
    try:
        anoNasc = int(input("Por favor, informe o seu ano de nascimento: "))
        if anoNasc < 1922 or anoNasc > 2021:
            print("Ano inválido!")
            anoNasc = True
        else:
            break

    except:
            print("Por favor, digite apenas números inteiros!")
            anoNasc = True



anoAtual = 2022
resposta = anoAtual - anoNasc

print("{} tem {} anos de idade.".format(nome,resposta))





















