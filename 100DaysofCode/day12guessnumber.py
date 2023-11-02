from art import logo4
import random
#from replit import clear #para limpar o terminal caso queira

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
tentativa=0
numero_secreto=random.randint(1,100)
vitoria=False
def start():
  print(logo4)
  print("Seja bem vindo(a) ao jogo Advinhe! \n")
  print("Advinhe um número de 1 a 100 aleatoriamente!")
  print("Escolha o nivel da dificuldade")
  print("1 - Fácil (10 tentativas)")
  print("2 - Difícil (5 tentativas)")
    
start()
eint=False
tadentro=False
while vitoria == False:
  while not eint == True:
    try:
      escolha=int(input("Escolha a opção: "))
    except:
      print('Digite 1 para Fácil ou 2 Para Difícil')
      continue
    if escolha == 1:
      tentativa=10
      eint=True
    elif escolha == 2:
      tentativa=5
      eint=True
  
  print(f"Você tem {tentativa} tentativas! Boa Sorte")
  #print(numero_secreto) # Para Mostra o número
  while tadentro == False:
    try:
      testa=int(input("Escolha um número de 1 a 100: "))
    except:
      print('ERRO!Digite apenas Números entre 1 a 100')
      continue
    if testa == numero_secreto:
      print("Parabéns, você acertou! \n")
      print(f'O Número secreto era o {numero_secreto} !!')
      tadentro=True
      vitoria=True
      break
    elif testa>numero_secreto:

      print('Número muito Alto')
    elif testa<numero_secreto:
     
      print("Número muito Baixo")
    if 100>=testa>=1: 
      tentativa -= 1
      if tentativa == 0:
        print('Você perdeu todas suas tentativas')
        print(f'O Número secreto era o {numero_secreto} !!')
        vitoria=True
        break
      elif tentativa >=1:
        
        print(f"Você tem {tentativa} tentativas agora")
    else:
      print('Você ultrapassou o limite de 1 a 100')