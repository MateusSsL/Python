import random
#Criando as imagens e lista com as imagens
erro = 'Por favor, escolha um número válido (entre 1 e 3): '
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagem = [erro,rock, paper , scissors] # lista com 4 elementos (1 ,3) sendo 0 msg de erro

while True: #Loop do jogo
    
        maquina = random.randint(1,3)#ignorando 0 pq é mensagem de erro(fiz para ficar melhor entendivel pra quem joga e codar)
        escolha = int(input("Escolha um número entre 1 a 3,sendo 1 pedra , 2 papel , 3 tesoura "))
        #testes de condição para o jogo acontecer
        if 1 <= escolha <= 3: #se for entre 1 a 3
            print("Você escolheu: {} O Computador: {} ".format(imagem[escolha] , imagem[maquina]))
        if escolha == maquina : #empate
            print('Empate!')
        if escolha == 0: #numero 0 para preencher a lista para a escolha da maquina
            print("Deseja terminar o jogo?")
        elif maquina == 3 and escolha == 1: #Pessoa:Pedra /// Maquina:Tesoura
            print('Você Ganhou!')
        elif maquina > escolha :
             print("Você Perdeu")
        elif escolha == 3 and maquina == 1:
             print('Você Perdeu')
        elif escolha > maquina and escolha < 4 : #condição para fechar o codigo sem escrever vc ganhou
             print ('Você ganhou')
        
        #como fechar o codigo
        if escolha < 1 or escolha > 3 : # se a escolha for menor q 1 ou maior ou igual a 4
             sair = input('Deseja fechar? S ou N ?').upper()
             if sair == 'S' :
                  break
        else:
            escolha = int(input("Escolha um número entre 1 a 3,sendo 1 pedra , 2 papel , 3 tesoura "))
        
        