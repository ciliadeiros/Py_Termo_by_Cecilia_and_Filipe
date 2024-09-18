from funcoes import (exibir_ranking,escolher_palavra,lista_de_letras,resetar_dados)
from colorama import Fore, Back, Style
import random

def jogar ():
    '''Esta função possui praticamente todo o jogo, de forma a eliminar qualquer variável global'''
    tentativas = {}
    resposta = escolher_palavra()
    for contador in range (1,6):
        letras_da_palavra = [] # Lista que será usada para armazenar as letras da palavra digitada pelo usuário
        arquivo = open('dicionario.txt',encoding='utf-8') #abre o dicionário
        lista = arquivo.readlines() #transforma o conteúdo do dicionário em lista
        arquivo.close()
        lista_nova = []
        for palavra in lista:
            lista_nova.append(palavra[:-1]) #tira o '\n' de todas as palavras da lista com as palavras do dicionário
        palavra = input(f'{contador}° tentativa: ').upper()
        print(palavra)
        print('')
        while len(palavra) != 5 or type(palavra) != str or palavra not in lista_nova:  # Verifica se tem menos ou mais letras que o ideal, se o tipo é string e se a palavra existe no dicionário
            palavra = input(f'{contador}° tentativa: ').upper()

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

    jogar ()
