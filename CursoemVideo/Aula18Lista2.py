#=============================== 084 ===================================
# listagem = list()
# final=list()
# mai=men=0
# print("-="*20)
# print('Pesagem')
# print("-="*20)
# while True:
#     final.append(str(input("Digite Seu nome: ").upper().strip()))
#     final.append(float(input("Digite seu peso: ")))
#     if len(listagem) == 0:
#         mai = men = final[1]
#     else:
#         if final[1] > mai:
#             mai=final[1]
#         if final[1] < men:
#             men=final[1]
#     listagem.append(final[:])
#     final.clear()
#     print('=-'*20)
#     resp = str(input("Quer continuar ? [S/N]"))
#     if resp in 'Nn':
#         break
# print('=-'*20)
# total=len(listagem)
# print(listagem)
# print(f'O total de cadastros foi : {total}')
# print(f'O maior peso foi {mai} kg, peso de: ',end="")
# for p in listagem:
#     if p[1] == mai:
#         print(f'{p[0]}',end=',')
# print(f'\nOs mais leve foram {men}kg, peso de: ',end=" ")
# for p in listagem:
#     if p[1] == men:
#         print(f'{p[0]}',end=',')
#=============================== 085 ===================================
# imp=list()
# par=list()
# lista=list()
# for i in range(0,7):
#     n=int(input("Digite um numero: "))
#     lista.append(n)
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         imp.append(n)
# lista=sorted(lista)
# imp=sorted(imp)
# par=sorted(par)
# print(f'Os numeros pares são: {par}')
# print(f'Os numeros impares são: {imp}')
# print(f'Os numeros registrados: {lista}')
#=============================== 086 e 087 ===================================        
# print("-="*20)
# print('Cubo 3x3')
# print("-="*20)
# cubo =[[0,0,0],[0,0,0],[0,0,0]]
# for l in range(0,3):
#     for c in range(0,3):
#         cubo[l][c]=int(input(f"Digite um valor para a posição [{l},{c}]: "))
# print("-=" * 20)
# soma=0
# terc=0
# mai=0
# for l in range(0,3):
#     for c in range(0,3):
#         print(f"[{cubo[l][c]:^4}]", end = "")
#         if cubo[l][c] % 2 ==0:
#             soma+= cubo[l][c]
#     print()
# for l in range(0,3):
#     terc += cubo[l][2]
# for c in range(0,3):
#     if c== 0 or cubo[1][c]>mai :
#      mai = cubo[1][c]
# print(f"\nA soma de todos os pares é: {soma}")
# print(f"O maior da Segunda linha é: {mai}")
# print(f"A soma da terceira coluna é: {terc}")
#=============================== 088 =================================== 
# from random import randint
# from time import sleep
# print("-="*20)
# print("{:-^40}".format(" Mega-Sena! "))
# print("-="*20)
# jogos=list()
# lista=list()
# tot=1
# qts= int(input("Me diga quantos jogos você gostaria de gerar: "))
# while tot <= qts:
#     cont= 0
#     while True:
#         num= randint(1,60)
#         if num not in jogos:
#             jogos.append(num)
#             cont+=1
#         if cont >=6:
#             break
#     jogos.sort()
#     lista.append(jogos[:])
#     jogos.clear()
#     tot += 1
# print('=-' * 4,f'Sorteando {qts} Jogos!','=-' * 4)
# for i,l in enumerate(lista):
#     print(f'Jogo{i+1}:{l}')
#     sleep(0.7)
#     print('=-'*20)
# print("{:-^40}".format(" Boa Sorte! "))
# print('=-'*20)
#=============================== 089 =================================== 
# listanomes=list()
# listanotas=list()
# listafinal=list()
# listamedia=list()
# print('=-'*20)
# print("{:-^40}".format(" Cadastro de Notas "))
# print('=-'*20)
# while True:
#     nome=str(input("Digite seu nome: "))
#     nota1=float(input("1 Nota :"))
#     nota2=float(input("2ª Nota :"))
#     med=(nota1+nota2)/2
#     listafinal.append([nome,[nota1 ,nota2], med])
#     resp=str(input("Quer continuar? [S/N]"))
#     if resp in 'Nn':
#         break
        
# print('-'*26)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*26)
# for i,a in enumerate(listafinal):
#     print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
# while True:
#     resp2=str(input("Quer Ver a note de algum aluno ou sair? [Sair/Nota]").title())
#     if resp2 in 'Sair':
#         break
#     else:
#         saber=int(input('Digite o numero do Aluno para saber as notas: '))
#         if saber <= len(listafinal) - 1:
#             print(f'Notas de {listafinal[saber][0]} são {listafinal[saber][1]}')
# print(f'{" Volte Sempre! ":=^40}')
#=============================== 089 =================================== 





 


