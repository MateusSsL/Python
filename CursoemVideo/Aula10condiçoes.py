import random
#Escreve um programa q escolha entre 0 a 5 e faça a pessoa tentar acertar o numero escolhido pela maquina
# computador = random.randint(0,6)
# print(computador)
# chute = int(input('digite um numero de 1 a 5 :'))
# while True:
#     if chute == computador:
#         print(f"Parabens vc acertou o nume escolhido é o numero {computador} !")
#         break
#     else:
#         chute = int(input('Numero errado tente novamente :'))

#verifique a velocidade de um carro e aplique multa de 7 reais para cada km a mais q o limite (80km/h)
# vel = int(input("qual é a velocidade em que o carro estava quando passou no radar: "))
# limite = 80
# multa = (vel - 80) * 7

# if vel >= 80:
#     print('A multa sera de : {:.2f} Reais'.format(multa))
# else:
#     print('Você estava dentro do limite da via')
          
#crie um programa que leia um numero e diga se ele é par ou impar
# numero = int(input('Digite um numero: ').strip())
# if numero % 2 == 0 or numero == 0:
#     print('Esse numero é PAR')
# else:
#     print('Esse numero é impar')
          
#crie um programa e diga se ele é bissexto ou não e quanto tempo falta para o proximo:
# ano = int(input('Digite um ano qualquer: ').strip())
# anobi = ano % 4
# dif = 4 - anobi
# if ano % 4 == 0 :
#     print('Esse é um ano Bissexto')
# else:
#     print(f'Esse não é um ano bissexto falta {dif} anos para o proximo ciclo')

#faça um programa q leia 3 numeros e diga qual o maior e qual o menor

def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 'Consigo formar um Triangulo !'
    else:
        return 'Impossivel formar um tringualo com esses numeros!'
numeros =input("Digite 3 numeros para formar um triangulo: ").strip().split()
numero = [int(transforma) for transforma in numeros]
a = numero[0]
b = numero[1]
c = numero[2]
print(a + b)
resultado = verificar_triangulo(a,b,c)
print(resultado)



# nome = str(input("Digite seu ID").title().strip())
# cadastro = []
# idade = str(input("Digite sua idade:").title().strip())
# cadastro.append(nome)
# cadastro.append(idade)
# print(cadastro)
# escolha = input('Digite seu ID e sua idade:').title()


#print(f'Ola {escolha}!' if escolha in cadastro[0] and idade [1] else 'Nome Errado')