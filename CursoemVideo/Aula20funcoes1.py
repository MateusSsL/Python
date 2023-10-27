#=============================== FUNCOES ===================================

from cev import mensagem,lin,centralizando

# mensagem(titulo=' Funções ')

# num=[4,8,9,2]
# soma(*num)
#=============================== 096 ===================================
#https://youtu.be/ezfr9d7wd_k?si=NSEldZTJR1VvbVJN
# def area(a,b):
#     ca = a*b
#     print(f'Area : {ca:.2f} m²')

# mensagem(titulo=" Controle de Terrenos ")
# a=float(input(f'Digite a Altura(m): '))
# b=float(input(f'Digite o Comprimento(m): '))
# area(a,b)

#=============================== 097 ===================================
# mensagem(titulo=" Escreva ")
# def escreva(nome):
#     print("-"*(len(nome)+5))
#     print(f"Olá,{nome} !")
#     print("-"*(len(nome)+5))
# nome=str(input("Digite seu nome:").title().strip())
# escreva(nome=nome)
#=============================== 098 ===================================
# mensagem(titulo=" Criando contador ")
# def contador(i,f,p):
#     if f > 0:
#         for x in range(i,f+1,p):
#             print(x,end=' ')
#     elif f <= 0:
#         for x in range(i,f-1,p):
#             print(x,end=' ')
#     print('Fim!')
# for t in range(0,3):
#     inicio=int(input("Digite o INICIO da contagem: "))
#     fim=int(input("Digite o FINAL da contagem: "))
#     passo=int(input("Digite de quanto ele vai pular entre os numeros: "))
#     if passo == 0:
#         p=1
#     print(f"Iniciando Contagem de {inicio} até {fim}, de {passo} em {passo}!")
#     lin()
#     contador(i=inicio,p=passo,f=fim)
#     lin()
#=============================== 099 ===================================
# mensagem(titulo=" Achando o Maior ")
# def maior(*valores):
#     m=1
#     for k in valor:   
#         if m <= k:
#             m = k
#     print(f'O maior numero entre os {len(valores)} digitados, foi o {m}!')

# valor=[]
# qt=int(input("Quantos valores você vai digitar?: "))
# for k in range(0,qt):
#     valor.append(int(input(f"Digite o {k+1}º valor: ")))
# lin()
# print(f'Os valores informados foram: {valor}')
# maior(*valor)
# centralizando(msg=' Final do Programa ')
#=============================== 100 ===================================
from random import randint
mensagem(titulo=" Gerando Lista com 5 Numeros ")
numeros=list()
def sorteia(list):
    for x in range(0,5):list.append(randint(0,50))
sorteia(numeros)
print(numeros)
def soma(somar):
    totpar= 0
    for k in somar:
        if k % 2 ==0:
            totpar += k
    print(f'A soma dos numeros pares na lista {somar} é : {totpar}')
soma(somar=numeros)







