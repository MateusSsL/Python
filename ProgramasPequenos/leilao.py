
import os
logo = '''
    ___________
    \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
    /_________\\
  .-------------.
/_______________\\
'''
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
maior=0
dados=list()
regist=dict()
print(logo)
print("-="*20)
print("{:-^40}".format(' Leilão online/Auction House '))
print("-="*20)
fim=False
while not fim:
    regist['Nome']=str(input("Digite seu nome/What's your name? ").title())
    regist['Oferta']=float(input("Qual será o valor do seu lance?/Bid "))   
    if regist['Oferta']> maior :
        maior=regist['Oferta']
        regist['Vencedor']=regist['Nome']
    dados.append(regist.copy())
    while True:
        resp=str(input("Mais alguem?/Another one to join?[S/N]").upper())
        if resp not in 'SN':
            resp=str(input("Tem outra pessoa para participar?[S/N]").strip().upper())
        elif resp =='S':  
            limpar_terminal()
            break
        elif resp == 'N':
            print(f"O vencedor é foi(winner) {regist['Vencedor']} !! \nCom um lance de(bid) {maior:.2f} $ !")
            fim=True
            break