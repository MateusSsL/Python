import random
from listaauxiliar import nomes
import os

palavra_secreta = random.choice(nomes).lower()
letras_acertadas = ''
numero_tentativas = 0
print('A Palavra é um NOME de uma pessoa, o nome está em minúsculo')
while True:
    letra_digitada = input('Digite uma letra: ').lower()
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta.upper())
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        break
            

            


    