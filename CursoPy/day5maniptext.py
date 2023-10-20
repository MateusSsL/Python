#programa q leia o nome e mostre em mausc/minus total de letras sem espaço
#quantas letras tem seu primeiro nome

#nome = input("Digite seu nome: ").strip().upper()
#print(nome)
#nomebaixo= nome.lower().strip()
#print(nomebaixo)
#total = len(nome) - nome.count(' ')
#print(total)
#primeironome = nome.split()
#print(len(primeironome[0]))

#============================================================
#faça um programa que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos sepadaos
#ex 1834 unidade:4 dezena:3 centena:8 milhar:1
# print("milhar:{} centena:{} dezena:{} unidade:{}".format(frase[0], frase[1], frase[2], frase[3]))
# frase = str(input("Digite um numero de 0 a 9999: "))
# frase = str(input("Digite um numero de 0 a 9999: "))

#============================================================
#cria um programa q leia o nome de uma cidade e diga se la começa
#ou nao com o nome 'SANTO'
# cidade = str(input("Qual o nome da sua ciade?: ").lower())
# if 'santo' in cidade :
#     print("Sim, sua cidade começa com Santo !")
# else:
#     print("Não, sua cidade não começa com Santo !")
#============================================================

#Faça um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra 'A'.
#em q posição ela apareece a primeira vez
#posicao da ultima vez
# texto = str(input("Digite uma texto qualquer: ").lower().strip())
# primeiro_a = texto.find('a')
# print(primeiro_a)
# total_a = texto.count('a')
# print(total_a)
# final_a = texto.rfind('a')
# print(final_a)
#print("A letra 'A' aparece: {} vezes!\nEla aparece primeiro na posição {} ! \nE por ultimo {} ! ".format(total_a, primeiro_a, final_a))

#============================================================
#cria um programa q leia o nome de uma pessoa e diga se ela tem
#ou nao o nome 'SILVA'
# nome = str(input('Digite seu nome: ').upper().strip())
# tems = 'SILVA' in nome
# if tems is True:
#     print("Seu nome tem Silva!")
# else:
#     print('Seu nome não tem Silva!')

#============================================================
#programa que leia o nome completo e mostre
#o primeiro e o ultimo nome separadamente
#ex ANA MARIA DE SOUZA
#primeiro: ANA
#ultimo: SOUZA

# nome= str(input('Qual é o seu nome? : ').lower().strip())
# lista = nome.title().split()
# print("Seu primeiro nome é: {}\nSeu ultimo nome é: {}".format(lista[0],lista[-1]))
