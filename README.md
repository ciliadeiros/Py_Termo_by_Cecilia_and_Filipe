import random
from colorama import Fore, Back, Style

palavras = ['risao', 'exito', 'termo', 'babar', 'beber', 'choro', 'circo', 'cloro']
resposta = random.choice(palavras) # Escolhe aleatoriamente uma palavra da lista, que será a reposta da rodada
letras_da_resposta = [] # Lista que será usada para armazenar as letras da resposta da rodada
for letra in resposta:
        letras_da_resposta.append(letra)

contador = 1
while contador < 6:
    letras_da_palavra = [] # Lista que será usada para armazenar as letras da palavra digitada pelo usuário
    palavra = input(f'{contador}° tentativa:  ')
    while len(palavra) != 5:   # Enquanto a palavra for menor ou maior que 5 letras, a pergunta irá se repetir
        palavra = input(f'{contador}° tentativa: ')
    for letra in palavra:
        letras_da_palavra.append(letra)
    for num in range (5):
        if letras_da_palavra[num] in resposta:
            if letras_da_palavra[num] == letras_da_resposta[num]:
                print(Back.GREEN + letras_da_palavra[num], end='')
            else:
                print(Back.YELLOW + letras_da_palavra[num], end='')
        else:
            print(Style.RESET_ALL + letras_da_palavra[num], end='')
    letras_da_palavra = []
    contador += 1
    print(Style.RESET_ALL, '\n')
    if palavra == resposta:
        break
letras_da_resposta = []

# Fazer a interface gráfica;
# Colocar mais palavras;
# Permitir que o usuário digite as palavras em maiúsculo ou minúsculo;
# Mostrar a palavra correta no final (caso o jogador perca);
# Colocar o alfabeto indicando quais letras ainda não foram usadas;
# Exibir a quantidade de tentativas no final:
    # Ex.:
    # 1 - X
    # 2 - X
    # 3 - !
