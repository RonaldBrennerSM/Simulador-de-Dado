import random

from lib.interface import *
from time import sleep

while True:
    resposta = menu(['\033[32mSim\033[m', '\033[31mNão\033[m'])

    if resposta == 1:
        n1 = random.randint(1, 6)
        print(f'\n\033[1;34mO seu dado deu: {n1}\033[m\n')

    elif resposta == 2:
        print('\nPrograma se encerrando...')
        sleep(1)
        print()
        cabeçalho('PROGRAMA ENCERRADO')
        break

    else:
        print(f'\n\033[1;31mERRO: Digite uma opção válida\033[m\n')