#exercicios 16 ao 19
#15 faça um programa q retorne o valor inteiro de um nemero real

#from math import floor
#numero2 = float(input("digite um numero: "))
#numero1 = numero2
#print("o numero {} , tem como numero inteiro : {} !".format(numero1, floor(numero2)))

#=================================================================
#16 faça um programa q retorne o valor da hipotenusa de acordo com o numero dos catetos recebidos do usuario

#from math import hypot, sqrt
#ca = float(input("Qual o valor do cateto adjacente :"))
#co = float(input("Qual o valor do cateto oposto :"))

#hip = math.sqrt(co ** 2 + ca **2)
#print("o valor da hipotenusa é : {:.2f}".format(hip))

#=================================================================
#17 programa q mostre o sen cosseno e tangente de um angulo qualquer

#from math import sin, tan, cos, radians
#ang = float(input("Digite seu angulo : "))
#seno = sin(radians(ang))
#coseno = cos(radians(ang))
#tangente = tan(radians(ang))
#print("o seno é {:.2f} , o coseno é {:.2f} , e a tangente é {:.2f}".format(seno, coseno, tangente))

#=================================================================
#18 programa para escolher randomicamente entre 4 pessoas

import random
n1 = str(input("Digite seu nome:"))
n2 = str(input("Digite seu nome:"))
n3 = str(input("Digite seu nome:"))
n4 = str(input("Digite seu nome:"))
nt = 4
lista = [n1, n2 , n3 , n4]
random.shuffle (lista)
print("Temos {} Alunos na lista e o sorteo foi: \n {} !".format(nt, lista))









