# lanche = 'Hambúrguer', 'Suco' , 'Pizza','Pudim','Batata Frita'
# # for comida in lanche:
# #     print(f'{comida}',end=" ")

# # for count in range (0,len(lanche)):
# #     print(f'Eu vou comer {lanche[count]}')
# # for pos,oque in enumerate(lanche):
# #     print(f'Eu vou comer {oque}, na posição {pos}')
# print(sorted(lanche))
# a = (1,2,3)
# b=(4,5,5,5,6,7)
# c=a+b
# print(c[0:4])
#======================== 072 ===========================
# numero=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoite','Dezenovo','Vinte')
# while True:
#     escolha=int(input("Digite entre 0 a 20: "))
#     if 20>=escolha>=0:
#         print(f'Você digitou o numero: {numero[escolha]}')
#     if escolha>20:
#         print("Você Escolheu um numero que não está entre 0 a 20\nSe desejar finalizar digite 99")
#     if escolha == 99:
#         break
# print("Fim")
#======================== 073 ===========================
# times=('Botafogo','Red Bull Bragantino','Grêmio','Palmeiras','Flamengo','Fortaleza','Fluminense','Athletico','Atlético','São Paulo','Cuiabá','Internacional','Cruzeiro','Corinthians','Santos','Bahia','Vasco','Goiás','Coritiba','América')
# print('''      [1] Para saber o Top 5 do cameponato.
#       [2] Os 4 últimos colocados da tabela.
#       [3] Uma lista com os Times em ordem alfabetica.
#       [4] A Posição do seu time.
#       [5] Para sair
#       ''')
# while True:
#     escolha=int(input('Escolha [0 a 5] : '))
#     if escolha == 1:print(times[0:5])
#     if escolha == 2:print(times[16:21])
#     if escolha == 3:print(sorted(times))
#     if escolha == 4:
#         time=str(input("Digite o nome do seu time: ").strip().title())
#         if time in times:print(f'Seu time está na {times.index(time)+1}ª posição')
#         else:print('Você digitou o nome do seu time errado, ou seu time não está na tabela')
#     if escolha == 5:break
# print("Fim")
#======================== 074 ===========================
# import random
# tupla = tuple(random.randint(1, 100) for _ in range(5))
# menor = 100
# maior = 0
# for x in tupla:
#     if x > maior:
#         maior = x
#     if x < menor:
#         menor = x
# print(sorted(tupla))
# print(f'O menor : {menor}!\nO maior é : {maior}!')
#======================== 075 ===========================
# list=[]
# pares=[]
# while True:
#     for n in range(1,6):
#         x=int(input(f"Digite o {n} valor: "))
#         list.append(x)
#     tupla=tuple(list)
#     nove=tupla.count(9)
#     if nove >= 1:print(f"O numero 9 apareceu {nove} vezes")
#     else:print('Não apareceu nenhum 9 na lista')
#     tres=tupla.index(3)
#     if tres>=1:print(f'O numero 3 apareceu primeiro na {tres+1}ª posição')
#     else:print('Não apareceu nenhum 3 na lista')
#     for par in list:
#         if par % 2 == 0:
#             pares.append(par)
#     print(f'O total de numeros pares foi de: {len(pares)} , foram eles: {pares}')
#     break
#======================== 076 ===========================
# lista = ('Pão',1,'Queijo',5.5,'Pizza',40,'Leite',3.75,'Peixe',16,'Frango',13,'Boscoito',4.5,'Carne',32.25)
# print("{:-^40}".format("-"))
# print("{:=^40}".format(" Lista Supermercado "))
# print("{:-^40}".format("-"))
# for x in range (0,len(lista)):
#     if x % 2== 0:
#         print(f'{lista[x]:.<40}',end="")
#     if x % 2 != 0:
#         print(f"R$ {lista[x]:.2f}")
# print("{:-^40}".format("-"))
# lista =('Ana','Pascoal','Ediane','Carmona','Fraga','Camila Ferraz','Laura','Alexandre','Escobar','Feliciano','Moises','Isac')
# for x in lista:
#     print(f"\nNa palavra {x.upper()} temos ", end="")
#     for letra in x:
#         if letra.lower() in 'aeiou':
#             print(letra, end=" ")


        
