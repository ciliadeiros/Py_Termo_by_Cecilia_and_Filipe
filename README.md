import random
from colorama import Fore, Back, Style
print('\n ______________________________________________________________________________________\n|                                                                                      |')
print('|   ______________   __________    __________      _____     _____    _____________    |')
print('|  |______________| |   _______|  |   _____  \    |     \   /     |  |   _______   |   | ')  
print('|       |    |      |   |_____    |  |_____|  |   |               |  |  |       |  |   | ')
print('|       |    |      |    _____|   |         _/    |    |\___/|    |  |  |       |  |   | ')
print('|       |    |      |   |______   |     _    \    |    |     |    |  |  |_______|  |   | ')
print('|       |____|      |__________|  |____| |____\   |____|     |____|  |_____________|   | ')
print('|                                                                                      |\n|______________________________________________________________________________________| ')
print('\nP E D R', Back.GREEN + ' A',Style.RESET_ALL +' -->', Back.GREEN + ' A', Style.RESET_ALL +' Faz parte da palavra e está na posição correta.', Back.YELLOW + '\n\nT', Style.RESET_ALL +' E R M O --> ', Back.YELLOW + ' T',Style.RESET_ALL +' Faz parte da palavra, mas em outra posição.', '\n\nP', Back.GREEN +' I L H A', Style.RESET_ALL +' --> P não está na palavra.')
print('\n______________________________________________________________________________________\n')


palavras = ['CENHO','CLORO','SORTE','PERTO','CERTO','VOLTA','PINHA','VERDE','CAIXA','LERDO','TRENA','FILHA','LIMBO','ALUNO','ILHAS','FILHO','SENHA','NARIZ','PORTA','HEROI','PALCO','MISTO','FALSO','MARCO','DOIDO','LOUCO','CERCA','LIMPO','BARCO','RISAO','FAIXA','EXITO','FORTE','TRATO','PORTE','PAPEL','LIVRO','PARTO','BISPO','BABAR','LINHA','BEBER','CORTE','GENRO','CHORO','MENTE','MORTE','CIRCO','VISCO','VENTO']
resposta = random.choice(palavras) # Escolhe aleatoriamente uma palavra da lista, que será a reposta da rodad
letras_da_resposta = [] # Lista que será usada para armazenar as letras da resposta da rodada
for letra in resposta:
        letras_da_resposta.append(letra)

tentativas = {}

contador = 1
while contador < 6:
    letras_da_palavra = [] # Lista que será usada para armazenar as letras da palavra digitada pelo usuário
    palavra = input(f'{contador}° tentativa: ').upper()
    print('')
    while len(palavra) != 5:   # Enquanto a palavra for menor ou maior que 5 letras, a pergunta irá se repetir
        palavra = input(f'{contador}° tentativa: ').upper()
    for letra in palavra:
        letras_da_palavra.append(letra)
    for num in range (5):
        if letras_da_palavra[num] in resposta:
            if letras_da_palavra[num] == letras_da_resposta[num]:
                print(Back.GREEN + letras_da_palavra[num], end='')
            else:
                print(Back.YELLOW + letras_da_palavra[num], end='')
        else:
            print(Back.BLACK + letras_da_palavra[num], end='')

    print(Style.RESET_ALL, '\n')
    if palavra == resposta:
        tentativas[contador] = '✅'
        break
    else:
        tentativas[contador] = '❌'
    letras_da_palavra = []
    contador += 1

letras_da_resposta = []
print('A resposta é:', Back.LIGHTBLUE_EX + resposta, Style.RESET_ALL)
print('Quantidade de tentativas:')
for chave, valor in tentativas.items():
    print(f'{chave} - {valor}')
