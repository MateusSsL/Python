############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random as rand
from art import logo3
import os

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cartasjogador= []
cartascomputador= []
ojogoacabou = False

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def dealer_cartas():
    '''Puxa um carta aleatoria do o deck'''
    carta = rand.choice(cartas)
    return carta

for _ in range(2):
    cartascomputador.append(dealer_cartas())
    cartasjogador.append(dealer_cartas())

def calculatotal(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def comparar(totaljogador,totalcomputador):
    if totaljogador > 21 and totalcomputador > 21:
        print("Vocês passaram do limite.Ambos Perderam 😤")
    
    if totaljogador == totalcomputador:
        print(f'Empate!')
    elif totaljogador==0:
        print('Você VENCEU por BlackJack!😎')
    elif totalcomputador==0:
        print('Você PERDEU, o oponente tem um BlackJack!😱')
    elif totaljogador>21:
        print(f'Você perdeu, ultrapassou o limite!😱')
    elif totalcomputador>21:
        print(f'Você Venceu,o Oponente ultrapassou o limite!😎')
    elif totaljogador>totalcomputador:
        print(f'Você Venceu!😎')
    else:
        print('Você Perdeu o Computador chegou mais perto de 21😱')
    

def jogar():
    limpar_terminal()
    print(logo3)
    cartasjogador= []
    cartascomputador= []
    ojogoacabou = False
    for _ in range(2):
        cartascomputador.append(dealer_cartas())
        cartasjogador.append(dealer_cartas())

    totaljogador= calculatotal(cartasjogador)
    totalcomputador=calculatotal(cartascomputador)
    while not ojogoacabou==True :

        totaljogador= calculatotal(cartasjogador)
        totalcomputador=calculatotal(cartascomputador)
        print(f'Suas Cartas{cartasjogador} , Total:{totaljogador}')
        print(f'1ª Carta do Computador:{cartascomputador[0]}')


        if totaljogador==0 and totalcomputador==0 and totaljogador>21:
                ojogoacabou = True

        else:
            continuar=input(f'Digite [S] para comprar outra carta, ou [N] para Parar: ').strip().upper()
            if continuar in 'SIM':
                cartasjogador.append(dealer_cartas())
                totaljogador= calculatotal(cartasjogador)
                if totaljogador > 21:
                    ojogoacabou=True
            elif continuar in 'NAO':
                ojogoacabou=True

    while totalcomputador !=0 and totalcomputador < 17:
        cartascomputador.append(dealer_cartas())
        totalcomputador=calculatotal(cartascomputador)

    print(f'Suas Cartas{cartasjogador} , Total:{totaljogador}')
    print(f'Computador: {cartascomputador}, Total:{totalcomputador}')

    print(comparar(totaljogador, totalcomputador))

while input('Quer jogar BlackJack? [S]ou[N] : ').upper() == 'S':
    limpar_terminal()
    jogar()




  
