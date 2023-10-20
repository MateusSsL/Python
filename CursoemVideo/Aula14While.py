#https://youtu.be/LH6OIn2lBaI?si=i2TZhqs0xg77mAlf&t=1661
# r = 'S'
# t = 0
# while r == "S":
#     n = int(input("Digite um numero: "))
#     r = input("Quer Continuar [S/N] ? ").upper()
#     t += n
# print(f"Fim , total acumulado : {t}")
# end = False
# erro = 0
# while not end:
#     sexo = input("Digite Qual o sexo da pessoa [M/F] : ").upper()
#     if sexo != "M" and sexo != "F":
#         erro += 1
#         print("Você digitou errado")
#     if erro >= 2:
#         end = True
# print("fim")
# from random import randint
# nrand = randint(0,10)
# tent= 7
# goal = False
# print(nrand)
# while not goal:
#     palpite = int(input("Tente Advinhar o numero de (0 a 10) : ").strip())
#     if palpite == nrand :
#         goal = True
#         print(f'Parabens você acertou com {tent} tentativas sobrando!')
#     if palpite != nrand :
#         tent -= 1
#         print(f"Você Errou tente novamente! agora vc tem {tent} vidas!")
#     if tent == 0:
#         goal=True
#         print("Você gastou todas as suas 7 vidas tente novamente!")
# print('Fim')

# def calc(somar,multiplicar,maior,sair):
#     somar = n1 + n2
#     multiplicar = n1 * n2
#     if n1 > n2:
#         maior = n1
#     if n2>n1:
#         maior = n2

# n1=int(input("Digite o primeiro valor: ").strip())
# n2=int(input("Digite o segundo valor: ").strip())
# resp = 0
# while not resp == 5:
#     print('''    [1] para Somar
#     [2] para Multiplicar
#     [3] para ver o Maior
#     [4] para novos numeros
#     [5] para sair''')
#     resp= int(input("Qual a sua opção: "))
#     if resp == 1:
#         soma =n1 + n2
#         print(f"A Soma é de {soma} !")
#     if resp == 2:
#         mult = n1 * n2
#         print(f"A Multiplicação é de {mult} !")
#     if resp == 3:
#         if n1>n2:
#             print(f'O maior numero é {n1}')
#         if n2>n1:
#             print(f'O maior numero é {n2}')
#     if resp == 4:
#         n1=int(input("Digite o primeiro valor: ").strip())
#         n2=int(input("Digite o segundo valor: ").strip())
# print('Fim do programa')

# from math import factorial
# n=int(input("Digite um numero: "))
# fatorial = factorial(n)
# print(f"O fatorial é {fatorial}")

# end=False
# f=1
# while not end:
#     n=int(input("Digite um numero: "))
#     for j in range(n-1, 0 , -1):
#         n *= j
#     end=True
# print(f'Fatorial = {n}')

#64
# print('Para pausar o programa digite 999 ')
# n1 = int(input("Digite um numero: "))
# n3 = n1
# n2=0
# calc = 1
# while n2 != 999:
#     n2 = int(input(f"Digite um numero para somar com {n3}: "))
#     n3 += n2
#     calc += 1
# n3 -= 999
# calc -= 1
# print(f"Você somou {calc} numeros e o resultado foi {n3}")
