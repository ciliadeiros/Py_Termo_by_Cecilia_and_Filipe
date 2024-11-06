from funcoes import (exibir_ranking,escolher_palavra,lista_de_letras,resetar_dados, remover_diacriticos)
from colorama import Fore, Back, Style
import random    

def jogar ():
    '''Esta função possui praticamente todo o jogo, de forma a eliminar qualquer variável global'''
    tentativas = {}
    resposta = escolher_palavra()
    for contador in range (1,6):
        letras_da_palavra = [] # Lista que será usada para armazenar as letras da palavra digitada pelo usuário
        arquivo = open('dicionario.txt',encoding='utf-8') #abre o dicionário
        lista = arquivo.readlines() # Transforma o conteúdo do dicionário em lista
        arquivo.close()
        lista_nova = []
        for palavra in lista:
            lista_nova.append(palavra[:-1]) # Tira o '\n' de todas as palavras da lista com as palavras do dicionário
        if contador > 1:
            print('-------------------------------------')
        while True: # Verifica algumas possibilidades de erro e impede o jogador de fazer jogadas impróprias
            palavra = input(f'{contador}° tentativa: ').upper()
            if len(palavra) != 5:
                print('\nSua palavra não contém 5 letras. Tente novamente!')
                continue
            if type(palavra) != str:
                print('\nEste jogo aceita apenas PALAVRAS como resposta. Tente novamente!')
                continue
            if palavra not in lista_nova:
                print('\nOps, sua palavra não está no nosso banco de dados! Tente digitá-la de outra forma ou tente outra PALAVRA.')
            else:
                print()
                break
        palavra = remover_diacriticos(palavra)
        resultado_da_tentativa = ''
        for letra in palavra: 
            letras_da_palavra.append(letra)
        for num in range (5): # Analisa a rodada e define uma palavra que possui uma letra específica dependendo so acerto, por exemplo "AAEPE", que signfica "acerto, acerto, erro, erro e parcial"
            if letras_da_palavra[num] in resposta:
                if letras_da_palavra[num] == lista_de_letras(resposta)[num]:
                    print(Back.GREEN + letras_da_palavra[num], end='')
                    resultado_da_tentativa += 'A'
                else:
                    print(Back.YELLOW + letras_da_palavra[num], end='')
                    resultado_da_tentativa += 'P'
            else:
                print(Back.BLACK + letras_da_palavra[num], end='')
                resultado_da_tentativa += 'E'
            
        print(Style.RESET_ALL, '\n')
        if palavra == resposta:
            tentativas[contador] = [palavra, resultado_da_tentativa]
            resetar_dados(letras_da_palavra)
            break
        else:
            tentativas[contador] = [palavra, resultado_da_tentativa]
            resetar_dados(letras_da_palavra)

    print('A resposta é:', Back.LIGHTBLUE_EX + resposta, Style.RESET_ALL)
    print('\nNÚMERO DA TENTATIVA | PALAVRA | RESULTADO (A- ACERTO, P- QUASE ACERTO, E- ERRADO) ')
    print('----------------------------------------------------------------------------------')
    for chave, valor in tentativas.items():
        print(f'{chave}                   | {valor[0]}   | {valor[1]}')
    print('')

    def cadastro_do_jogador():
        '''Faz o cadastro do jogador; Caso o jogador erre todas as tentativas, esse cadastro não é exibido.'''
        pontuacao = str(len(tentativas))
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

    if len(tentativas) == 5:
        if tentativas[5] != 'AAAAA':
            print('\n*************** RANKING ***************\n')
            print(exibir_ranking())
            print('\n***************************************')
        else:
            cadastro_do_jogador()

            print('\n*************** RANKING ***************\n')
            print(exibir_ranking())
            print('\n***************************************')
    else:
            cadastro_do_jogador()

            print('\n*************** RANKING ***************\n')
            print(exibir_ranking())
            print('\n***************************************')
            
if __name__ == "__main__":
    while True:

        print('\n ________________________________________________________________________________________________________________\n|                                                                                                                |')
        print('|   __________    ___    ___      ____________   __________    __________     _____     _____    _____________   |')
        print('|  |    ___   \\  |   \\__/   |    |____________| |   _______|  |   _____  \\   |     \\___/     |  |   _______   |  | ')  
        print('|  |   |___|   |  \\        /         |    |     |   |_____    |  |_____|  |  |               |  |  |       |  |  | ')
        print('|  |     _____/    \\      /          |    |     |    _____|   |         _/   |    |\\___/|    |  |  |       |  |  | ')
        print('|  |    |           |    |    __     |    |     |   |______   |     _    \\   |    |     |    |  |  |_______|  |  | ')
        print('|  |____|           |____|   |__|    |____|     |__________|  |____| |____\\  |____|     |____|  |_____________|  | ')
        print('|                                                                                                                |')
        print('|________________________________________________________________________________________________________________|                                                                                      ')
        print('\nCOMO FUNCIONA?\nO PY.TERMO se trata de uma adaptação do jogo TERMO, de FERNANDO SERBONCINI, para a linguagem de python. O jogo\nconsiste em DESCOBRIR A PALAVRA CERTA em apenas 5 tentativas. Será que você será capaz de acertar?!\n\nEXEMPLOS:\nP E D R', Back.GREEN + ' A',Style.RESET_ALL +' -->', Back.GREEN + ' A', Style.RESET_ALL +' Faz parte da palavra e está na posição correta.','\n\n',Back.YELLOW+'T', Style.RESET_ALL +' E R M O --> ', Back.YELLOW + ' T',Style.RESET_ALL +' Faz parte da palavra, mas em outra posição.', '\n\nP', Back.GREEN +' I L H A', Style.RESET_ALL +' --> P não está na palavra.')
        print('\n⚠️  IMPORTANTE:\n  * Tamanho da palavra: 5 letras\n  * Quantidade de tentativas: 5\n')
        print('______________________________________________________________________________________\n')

        jogar ()
