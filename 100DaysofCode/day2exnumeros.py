#exercicios
#faça um programa que leia um numero e de na tela seu sucessor e seu antecessor

#numero = int(input("Digite um numero ! : "))
#ante = numero - 1
#sece = numero +1
#print("o antecessor do numero {} é {} e seu sucessor é o numero {}" .format(numero, ante, sece))

#=================================================================
#faça um programa q leia um numero e da seu dobro,tripo e sua raiz quadrada

#numero = int(input("escola um numero: "))
#dobro = numero * 2
#triplo = numero * 3
#raiz = numero ** 2
#print("seu dobro é: {} , o triplo é: {} e sua raiz é: {}".format(dobro, triplo, raiz))

#=================================================================
#calcula duas notas de um aluno e de sua média

#n1 = int(input("qual sua primeira nota :"))
#n2 = int(input("e sua segunda nota? :"))
#calc = (n1 + n2) / 2
#print("sua média é {} !".format(calc))

#=================================================================
#faça um programa q leia um numero na tela e de sua tabuada

num = int(input("Qual numero que você quer saber a tabuada? : "))
xis = 1
tabuada = num * xis

while xis <= 10 :
    print("{} X {} = {}".format(num, xis, tabuada))
    xis = xis + 1
    tabuada = num * xis

#=================================================================
#faça um aumento de 15% no salario atual de uma pessoa

#sal = float(input("Qual é o seu salario atual: "))
#calculo = float(sal * 1.15)
#calc = "{:.2f}".format(calculo)
#print(f"O seu salario com o novo aumento fica : {calc} Reais")