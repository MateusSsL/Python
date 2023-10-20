#Contagem regressiva
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from time import sleep
# for c in range(10,-1,-1):
#     print(c)
#     sleep(0.5)
# print('BOOM BOOM POOWH')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Mostrador de numeros pares
# for x in range (0,51,2):
#     print(x, end = " ")
# print(" \nFIM")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #Tabuado com for
# n = int(input("Digite um numero qualquer:").strip())
# for l in range (1,11):
#     print(f'\n{n} x {l} = {n*l}')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# c = 0
# for x in range(1,7):
#     n = int(input(f"Digite o {x} numero: "))
#     if n % 2 == 0:
#         c += n
# print(f"A soma final dos numeros pares foi de: {c}")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
# ptermo = int(input("Digite o primeiro termo da PA: "))
# r =int(input("Digite a Razão da sua PA: "))
# res = ptermo
# for x in range(1,11):
#     print(res,end=" ")
#     res += r
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# n = int(input("Digite um numero qualquer :"))
# tot = 0
# for x in range(1,n+1):
#     if n % x == 0:
#         tot += 1
# if tot > 2:
#         print('Esse numero não é Primo')
# else:
#         print("Primo")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
# print(f'O maior peso foi de {max(pesos)}Kg\nO menor foi de {min(pesos)}Kg!')
#reveja o ex 56

    
