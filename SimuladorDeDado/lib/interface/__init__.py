def linha(tam = 30):
    return '\033[35m-\033[m' * 30


def cabeçalho(txt):
    print(linha())
    print(txt.center(32))
    print(linha())


def menu(lista):
    cabeçalho('DESEJA GIRAR O DADO?')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    resposta = leiaInt('Digite sua opção: ')
    return resposta


def leiaInt(NI):
    while True:
        try:
            NI = int(input('Digite sua opção: '))
        except:
            print('\n\033[1;31mERRO: por favor digite um número inteiro\033[m\n')
            continue
        else:
            return NI