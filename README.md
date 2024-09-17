from funcoes import (exibir_ranking,escolher_palavra,lista_de_letras,resetar_dados)
from colorama import Fore, Back, Style
import random

'''Essa função precisa estar dentro do código principal pois ela depende da variável 'palavra', a qual é definida neste código'''
def comparar_palavras (palavra, resposta):
    '''Função para comparar a palavra digitada pelo usuário com a resposta'''
    for letra in palavra:
        letras_da_palavra.append(letra)
    for num in range (5):
        if letras_da_palavra[num] in resposta:
            if letras_da_palavra[num] == lista_de_letras(resposta)[num]:
                print(Back.GREEN + letras_da_palavra[num], end='')
            else:
                print(Back.YELLOW + letras_da_palavra[num], end='')
        else:
            print(Back.BLACK + letras_da_palavra[num], end='')
            
if __name__ == "__main__":

    print('\n ______________________________________________________________________________________\n|                                                                                      |')
    print('|   ______________   __________    __________      _____     _____    _____________    |')
    print('|  |______________| |   _______|  |   _____  \    |     \___/     |  |   _______   |   | ')  
    print('|       |    |      |   |_____    |  |_____|  |   |               |  |  |       |  |   | ')
    print('|       |    |      |    _____|   |         _/    |    |\___/|    |  |  |       |  |   | ')
    print('|       |    |      |   |______   |     _    \    |    |     |    |  |  |_______|  |   | ')
    print('|       |____|      |__________|  |____| |____\   |____|     |____|  |_____________|   | ')
    print('|                                                                                      |')
    print('|______________________________________________________________________________________|                                                                                      ')
    print('\nP E D R', Back.GREEN + ' A',Style.RESET_ALL +' -->', Back.GREEN + ' A', Style.RESET_ALL +' Faz parte da palavra e está na posição correta.','\n\n',Back.YELLOW+'T', Style.RESET_ALL +' E R M O --> ', Back.YELLOW + ' T',Style.RESET_ALL +' Faz parte da palavra, mas em outra posição.', '\n\nP', Back.GREEN +' I L H A', Style.RESET_ALL +' --> P não está na palavra.')
    print('\n⚠️  Tamanho da palavra: 5 letras\n')
    print('\n______________________________________________________________________________________\n')

    tentativas = {}
    resposta = escolher_palavra()
    for contador in range (1,6):
        letras_da_palavra = [] # Lista que será usada para armazenar as letras da palavra digitada pelo usuário
        palavra = input(f'{contador}° tentativa: ').upper()  
        print('')
        while len(palavra) != 5 or type(palavra) != str:  # Verifica se tem menos ou mais letras que o ideal e se o tipo é string
            palavra = input(f'{contador}° tentativa: ').upper()
    
        
        comparar_palavras(palavra, resposta)
                    
        print(Style.RESET_ALL, '\n')
        if palavra == resposta:
            tentativas[contador] = '✅' # Faz um dicionário que recebe o número da tentativa e se o usuário acertou ou não. Ex.: 1 - ❌, 2 - ✅
            resetar_dados(letras_da_palavra)
            break
        else:
            tentativas[contador] = '❌'
            resetar_dados(letras_da_palavra)

    print('A resposta é:', Back.LIGHTBLUE_EX + resposta, Style.RESET_ALL)
    print('Quantidade de tentativas:')
    for chave, valor in tentativas.items():
        print(f'{chave} - {valor}')
    print('')

    def cadastro_do_jogador():
        pontuacao = str(list(tentativas.keys())[-1])
        verificacao = input('Deseja cadastrar-se no jogo? Sim(S) | Não(N): ').upper()
        while verificacao != 'S' and verificacao != 'N':
            verificacao = input('Deseja cadastrar-se no jogo? Sim(S) | Não(N): ').upper()
        if verificacao == 'N':
            return
        nome = input('Digite seu nome: ')
        while type(nome) != str:
            nome = input('Digite seu nome: ')
        arquivo = open('ranking.txt','a',encoding='utf-8') #abre arquivo com as regras da gramática br
        arquivo.write(nome + '\n')#adiciona a variável nome no arquivo
        arquivo.write(pontuacao + '\n')
        arquivo.close()
        resetar_dados(tentativas)

    cadastro_do_jogador()

    print('\n*************** RANKING ***************\n')
    print(exibir_ranking())
    print('\n***************************************')
