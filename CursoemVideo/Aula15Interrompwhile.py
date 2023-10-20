#===============================067===============================
# n = 2
# while n > 0:
#     n= int(input("Digite um numero: "))
#     for x in range(0,11):
#         calc=x*n
#         if n>0:
#             print(f"{x} X {n} = {calc}")
# print("fim")
#===============================068===============================
# from random import randint
# perdeu = False
# escolha = ""
# while not perdeu:
#     n=int(input("Digite um numero: "))
#     pi=str(input('Escolha [P] PAR ou [I] Impar : ').upper())
#     comp= randint(0,10)
#     soma= n+comp
#     if soma % 2 == 0:
#         escolha = "Par"
#     else:
#         escolha = 'Impar'
#     print(f"O computador escolheu {comp} a soma foi {soma}! então deu {escolha} !")
#     if pi in escolha:
#         print('Você venceu! jogue novamente!')
#     else:
#         print('Você Perdeu!')
#         perdeu=True
#===============================070===============================
# cont = False
# prod1000=0
# total=0
# menor=1000
# mprod= ''
# print("{:-^40}".format("Caixa do Supermercado"))
# while not cont:
#     n=str(input("Qual é o NOME do produto: "))
#     p=int(input("Digite o PREÇO do produto:$ "))
#     if p>0:
#         total += p
#     if p<menor:
#         menor = p
#         mprod = n
#     if p>=1000:
#         prod1000 += 1
#     esc=str(input("Deseja Cadastrar outro Produto?[S/N]").strip().upper()[0])
#     if esc == 'S':
#         cont=False
#         print("{:-^40}".format("Adicionando outro Item"))
#     else:
#         print("{:-^40}".format("Finalizamos a Compra"))
#         print(f'(A) O Total gasto na compra foi de {total:.2f} Reais')
#         print(f'(B) O Total de produtos acima de 1000 Reais foi de {prod1000} produtos')
#         print(f'(C) O Produto mais barato na compra foi {mprod} por {menor} Reais')
#         cont=True
#===============================071===============================
# print("=" * 30)
# print('{:=^40}'.format("Caixa Eletronico"))
# print("=" * 30)
# sac=int(input("Que valor você deseja sacar? R$: "))
# total = sac
# cel = 50
# contcel = 0
# while True:
#     if total>=cel:
#         total -= cel
#         contcel += 1
#     else:
#         print(f'Total de {contcel} células de R${cel}Reais')
#         if cel==50:
#            cel ==20
#         elif cel == 20:
#            cel==10
#         elif cel==10:
#            cel==1
#         contcel = 0

#         if total == 0:
#            break


    




