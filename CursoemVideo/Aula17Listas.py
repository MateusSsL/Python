#=============================== 078 ===================================
# lista = []
# for x in range(0,5):
#     lista.append((input("Digite um numero: ")))
# lista=sorted(lista)
# print(lista)
# print(f"O maior numero é {lista[0]} e o menor é {lista[-1]}")
#=============================== 079 ===================================
# lista=[]
# while True:
#     n=(int(input("Digite um numero: ")))
#     if n not in lista:
#         lista.append(n)
#     elif n in lista:
#         print("Você digitou um valor que já esta na lista.")
#         resp = str(input("Para Sair Digite: [S/N] ").strip().upper())
#         if resp == 'S':
#             break
# print('=-*30)
# print(f"Os numeros digitados foram : {lista}")
#=============================== 080 ===================================
#Crie um programa que leia 5 numeros e adicione um uma lista já na ordem crescente
#no final mostre a lista ordenada
# print('=-'*30)
# lista=[]
# for x in range(0,5):
#     n = int(input("Digite um numero :"))
#     if x==0 or n>lista[-1]:# se o numero for o primeiro ou maior q o ultimo da lista
#         lista.append(n)
#     else:
#         pos = 0 #posição
#         while pos<len(lista):# de 0 até a ult posição
#             if n <= lista[pos]: #verificar se o numero que for inserir é menor ou igual ao que ja tem na lista
#                 lista.insert(pos,n)
#                 break
#             pos += 1 #para subir a posição
# print('=-'*30)
# print(f"Os valores em ordem são: {lista}")
#=============================== 081 ===================================
# lista=[]
# print('=-'*20)
# print("{:-^40}".format(" Digite 99 para Sair "))
# print('=-'*20)
# while True:
#     n=int(input("Digite um numero: "))
#     lista.append(n)
#     if n == 99:
#             print(f"Foram digitados: {len(lista)} numeros!")
#             lista.sort(reverse=True)
#             print(lista)
#             if 5 in lista:
#                   print(f'O numero 5 foi digitado: {lista.count(5)} vezes')
#             else:
#                   print("Não foi encontrado nenhum numero 5")
#             break
#=============================== 082 ===================================
# lista=[]
# listapar=[]
# listaimp=[]
# print('=-'*20)
# print("{:-^40}".format(" Digite 99 para Sair "))
# print('=-'*20)
# while True:
#     n=int(input("Digite um numero: "))
#     lista.append(n)
#     if n % 2 == 0:
#         listapar.append(n)
#     else:
#         listaimp.append(n)
#     if n == 99:
#         break
# list.sort(lista)
# list.sort(listapar)
# list.sort(listaimp)
# print(f"Listagem: {lista} \nPares: {listapar}\nImpares: {listaimp}")
#=============================== 082 ===================================
# print('=-'*20)
print('=-'*20)
expr=str(input("Digite uma expressão: "))
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está incorreta!")

    

    