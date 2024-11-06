import random
from colorama import Fore, Back, Style
open('ranking.txt','a').close

def exibir_ranking ():
    arquivo = open('ranking.txt',encoding='utf-8') # Abre o arquivo só para leitura
    linhas = arquivo.readlines() # Transforma o conteúdo do arquivo em lista
    arquivo.close()
    ranking = []
    for i in range(0, len(linhas),2):# Para cada elemento de dois em dois no alcance de linhas
        nome = linhas[i][:-1] #O nome será o elemento de linhas na posição i menos o último caractere
        pontuacao = int(linhas[i+1][:-1])# A pontuação será o elemento na posição i+1 visto que está em uma posição que o for não alcança 
        nome_pontuacao = [pontuacao, nome]# Lista com um nome e uma pontuação
        ranking.append(nome_pontuacao)
        sorted(ranking)
    print('----------------------------------------------------------------------------------')
    print('JOGADOR:                          | PONTUAÇÃO:')
    contador = len(ranking)
    for l in ranking:
        for c in ranking:
            print()

    return sorted(ranking) # Retorna ranking de maior para menor valor

def remover_diacriticos (palavra):
    '''Remove os acentos e os sons nasais das palavras. Ele analisa a palavra letra por letra, verificando se há acentos e sons nasais, e depois remove-os e salva cada letra em uma nova string.'''
    palavra_nova = ''
    for letra in palavra:
        if letra in 'ÁÀÃÂ':
            palavra_nova += 'A'
        elif letra in 'ÓÔÒÕ':
            palavra_nova += 'O'
        elif letra in 'ÉÊÈ':
            palavra_nova += 'E'
        elif letra in 'ÙÚÛ':
            palavra_nova += 'U'
        elif letra in 'ÍÌÎ':
            palavra_nova += 'I'
        elif letra == 'Ç':
            palavra_nova += 'C'
        else:
            palavra_nova += letra
    return palavra_nova
    
def escolher_palavra (): 
    '''Função que escolhe uma palavra da lista de palavras para ser a resposta da rodada'''
    arquivo = open('palavras.txt', encoding='utf-8') # Puxa o arquivo onde estão as palavras
    palavras = arquivo.readlines()
    arquivo.close()
    resposta = random.choice(palavras)[:-1]
    print('Para facilitar nos testes:', resposta)
    resposta = remover_diacriticos(resposta)
    return resposta

def lista_de_letras (palavra):
    '''Função que coloca cada letra da resposta em uma lista que, depois, servirá para comparação com a tentativa do usuário'''
    letras_da_resposta = []
    for letra in palavra:
        letras_da_resposta.append(letra)
    return letras_da_resposta

def resetar_dados (dados):
    '''Esta função tem uma finalidade bem específica de resetar a lista que contém as letras da palavra digitada pelo usuário e também de resetar, ao fim da rodada, o dicionário que contém a quantidade de tentativas e quais foram erros e acertos. Isto foi feito em forma de função como uma forma de limpar o código, evitando a necessidade de fazer outra lista e outro dicionáio de mesmo nome, porém sem conteúdo. '''
    if type(dados) == list:
        dados = []
    elif type(dados) == dict:
        dados = []
    return dados
