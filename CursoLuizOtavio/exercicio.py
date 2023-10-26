"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
"""
# n=input("Digite um número inteiro: ")
# inteiro=False
# if n.isnumeric():
#     inteiro=True
#     nint=int(n)
#     if nint % 2 ==0:
#         print(f"{nint} é PAR")
#     else:
#         print(f"{nint} é IMPAR")
# elif inteiro is False:
#     nfloat=float(n)
#     print(f"{nfloat:.1f} é um numero flutuante!")
# else:
#     print(f"você não digitou um numero")
    


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora=input("Que horas são: ")
# saudar=''
# try:
#     hora_int=int(hora)
#     if 11>=hora_int>=0:
#         saudar='Bom Dia'
#     elif 17>=hora_int>=12:
#         saudar='Boa Tarde'
#     elif 24>=hora_int>=18:
#         saudar='Boa noite'
#     print(f"{saudar}")
# except:
#     print('Você não digitou um horario valido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome=input('Digite seu nome: ')
# tamanho_nome=len(nome)

# if tamanho_nome>1:
#     if tamanho_nome<=4:
#         texto='curto'
#     elif 6>=tamanho_nome>4:
#         texto='normal'
#     elif tamanho_nome>6:
#         texto='muito grande'
#     print(f'Seu nome é {texto}')
# else:
#     print('digite um nome maior')
